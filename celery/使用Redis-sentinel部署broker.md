# 问题：
在使用redis做broker时，为了保证高可用性，一般采用一主多从的部署方式，这时候就需要master故障，slave可以变成master。

# 解决办法：
redis高可用方案中有一种sentinel方式，
可以帮助在master故障后，将slave转成master。
并且celery是支持sentinel模式的。

```
app = Celery('app')
app.config_from_object('celeryconfig')
sentinels = [
    'sentinel://192.168.31.126:26379/2',
    'sentinel://192.168.31.129:26379/2',
    'sentinel://192.168.31.130:26379/2',
]
app.conf.broker_url = ';'.join(sentinels)
app.conf.broker_transport_options = { 'master_name': 'mymaster'}
```
> 在配置过程当中遇到了几种问题
> redis-server的配置中绑定了IP，并且设置了密码
> 在sentinel配置中也配置了master的密码，但是使用
> celery的时候就是不能正确连接。
> 最后没有办法，只能把redis配置中的密码去掉，
> 同时关闭了配置中的保护模式

redis.conf
```
port 7000
# bind 192.168.31.129
daemonize yes
protected-mode no
pidfile "/var/run/redis_7000.pid"
appendonly yes
# masterauth "123456"
# requirepass "123456"
```

sentinel.conf
```
port 26379
# bind 192.168.31.129
# requirepass 123456

daemonize yes
protected-mode no
sentinel myid 980504a32d5a5fe6984124d6f25af5c77a860eb3
sentinel deny-scripts-reconfig yes
sentinel monitor mymaster 192.168.31.129 7000 2
# sentinel auth-pass mymaster 123456
```
