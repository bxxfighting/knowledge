# 问题：
将python web服务器通过wsgi启动到了8000端口  
现在用nginx将80端口的请求转发到8000

# 解决办法：
/etc/nginx/sites-enabled/demo.conf
```
server {
        listen 80;
        listen [::]:80;

        server_name buxingxing.com;

        root /home/xx/workspace/demo/;
        index index.html;

        location / {
                proxy_redirect off;
                proxy_pass http://localhost:8000;
        }
}
```

> 这里的配置只是完成最简单的基础功能  
> 未涉及nginx的其它配置