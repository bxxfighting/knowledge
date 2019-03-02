# 问题：
现在我有三台应用服务器，想对这三台进行负载均衡

# 解决办法：
/etc/nginx/sites-enabled/demo.conf
```
upstream nodes {
    server 192.168.31.82;
    server 192.168.31.126;
    server 192.168.31.130;
}

server {
    listen 80;
    listen [::]:80;

    server_name buxingxing.com;
    location / {
        proxy_pass http://nodes;
    }
}
```
如果我们的机器性能不统一，可以配置不同机器不同权重，默认权重为1，值越大权重越高
```
upstream nodes {
    server 192.168.31.82 weight=10;
    server 192.168.31.126 weight=20;
    server 192.168.31.130 weight=30;
}
```
配置根据ip的hash值来分配，这样同IP的就会落到同一台服务器上
```
upstream nodes {
    ip_hash;
    server 192.168.31.82;
    server 192.168.31.126;
    server 192.168.31.130;
}
```
fair模式是根据服务器的响应时间来分配，时间短的优先分配，但是这个需要下载第三方模块支持
```
upstream nodes {
    fair;
    server 192.168.31.82;
    server 192.168.31.126;
    server 192.168.31.130;
}
```
url_hash模式可以根据请求的url来分配，同请求分配到同服务器上，但是这个也需要下载第三方模块支持
```
upstream nodes {
    hash $request_uri;
    hash_method crc32;
    server 192.168.31.82;
    server 192.168.31.126;
    server 192.168.31.130;
}
```
backup标志，代表如果别的都不行了，就它上
```
upstream nodes {
    server 192.168.31.82;
    server 192.168.31.126;
    server 192.168.31.130 backup;
}
```
现在负载均衡有了，我们来限制一下同IP的访问次数
```
upstream nodes {
    server 192.168.31.82;
    server 192.168.31.126;
    server 192.168.31.130;
}

server {
    listen 80;
    listen [::]:80;

    server_name 192.168.31.89;
    limit_req zone=one burst=5 nodelay;
    location / {
        proxy_pass http://nodes;
    }
}

limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;
```
> $binary_remote_addr为二进制远程地址
> zone=one定义zone名称
> 10m分给此zone10M的内存，用来存储二进制远程地址（会话），1M内存可以存储16000会话
> rate=10r/s，限制每秒10个请求
> burst=5为允许超过限制数+5个请求（只有当之前的几秒内不足10个请求时，把剩下的名额给了接下来的几秒）
> nodelay就是不延迟处理，直接返回503

上面限制了1秒内的访问次数，现在限制同一时间的并发数
```
upstream nodes {
    server 192.168.31.82;
    server 192.168.31.126;
    server 192.168.31.130;
}

server {
    listen 80;
    listen [::]:80;

    server_name 192.168.31.89;
    limit_conn addr 1;
    location / {
        proxy_pass http://nodes;
    }
}

limit_conn_zone $binary_remote_addr zone=addr:10m;
```

#### 为了测试以上内容需要一个并发的访问
```
import time
import asyncio
from aiohttp import ClientSession

tasks = []
url = "http://192.168.31.89"
async def hello():
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()

def run():
    for i in range(1000):
        task = asyncio.ensure_future(hello())
        tasks.append(task)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))
```