# 问题：
当celery使用redis当broker时，单机容易出现问题，因此需要高可用

# 解决办法：
在celery中没有使用redis cluster的办法，只能使用redis sentinel
```
app.conf.broker_url = 'sentinel://localhost:26379;sentinel://localhost:26380;sentinel://localhost:26381'
app.conf.broker_transport_options = { 'master_name': "mymaster" }
```