# 问题:
redis集群的主要作用是，当存储大量数据时，单台服务器无法承载时使用

# 解决办法：
redis.conf配置内容:
```
port 10000
daemonize yes  //redis后台运行
pidfile /var/run/redis_10000.pid
cluster-enabled  yes  //开启集群  把注释#去掉
cluster-config-file  nodes_7000.conf  //集群的配置  配置文件首次启动自动生成 7000,7001,7002
cluster-node-timeout  15000  //请求超时  默认15秒，可自行设置
appendonly  yes
```
执行:
```
redis-server redis.conf
```
redis我是通过sudo apt install redis-server安装的，没有redis-trib.rb
因此又下载了redis安装包
```
wget https://codeload.github.com/antirez/redis/tar.gz/3.0.6
```
找到里面的redis-trib.rb文件放到了/usr/bin目录下
然而执行，还需要安装ruby，
```
sudo apt install ruby
sudo gem install redis
```
```
redis-trib.rb  create  --replicas  1  192.168.31.126:10000
```

参考内容：
https://www.cnblogs.com/wuxl360/p/5920330.html
