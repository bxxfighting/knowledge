# 问题:
redis一主多从架构，如果master失效，如何使slave变成master

# 解决办法:
redis.conf内容:
```
port 10000
# 这里这个IP绑定一定要绑，要不然用其它机器访问# 时，会告诉你得绑定IP，并且设置认证密码
bind 192.168.31.129
# 这个应该是告诉这个节点master的认证密码
masterauth 123456
# 这个应该是设置自己这个节点的密码
requirepass 123456
daemonize yes
pidfile /var/run/redis_10000.pid
appendonly yes
```

```
port 10001
bind 192.168.31.126
# 这个应该是告诉这个节点master的认证密码
masterauth 123456
# 这个应该是设置自己这个节点的密码
requirepass 123456
daemonize yes
pidfile /var/run/redis_10001.pid
appendonly yes
# 指定为10000这台的slave
slaveof 127.0.0.1 10000
```

```
port 10002
bind 192.168.31.130
# 这个应该是告诉这个节点master的认证密码
masterauth 123456
# 这个应该是设置自己这个节点的密码
requirepass 123456
daemonize yes
pidfile /var/run/redis_10002.pid
appendonly yes
slaveof 127.0.0.1 10000
```

下载:
```
wget https://codeload.github.com/antirez/redis/tar.gz/3.0.6
```
将里面的sentinel.conf文件拷贝出来使用
```
daemonize yes 
port 10010
bind 192.168.31.129
#指定别名  主节点地址  端口  哨兵个数（有几个哨兵监控到主节点宕机执行转移）
sentinel monitor mymaster 192.168.31.129 10000 2
# 多久未检测到master的心脏帧就更换master
sentinel down-after-milliseconds mymaster 3000
#选举出新的主节点之后，可以同时连接从节点的个数
sentinel parallel-syncs mymaster 1
#如果10秒后,master仍没活过来，则启动failover,默认180s  
sentinel failover-timeout mymaster 10000
sentinel auth-pass mymaster 123456
```

启动：
查看主从状态
```
info replication
```


> 这里要注意的就是redis.conf和sentinel.conf中  
> 都要设置上bind ip和密码

参考内容：
https://blog.51cto.com/dengaosky/2091877
