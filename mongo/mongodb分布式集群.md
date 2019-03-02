# 问题：
mongodb通过复制来实现高可用，而如果应对大数据和高并发呢  
Shard

# 解决办法：
> 操作系统：Ubuntu 16.04 server 64bit  
> mongodb version: v4.0.6  

mongo通过Shard来进行分布式部署，其中涉及到config服务器、shard服务器、mongos服务器  
其中config服务器都样需要部署成复制集，每一个Shard都是一个复制集，mongos为操作mongodb的入口  
三台机器：
```
A：192.168.0.130
B：192.168.0.131
C: 192.168.0.132
```

三台机器上目录结构统一创建：  
主目录下创建目录```mongodb```目录，  
然后在```mongodb```目录创建四个目录```configs、mongos、rs0、rs1```，  
同时在这四个目录下再分别创建```data、log```目录

#### 一、先来完成配置服务器的复制集在三台机器的目录```~/mongodb/configs/```下均创建```mongod.conf```文件，并写入如下内容：
```
storage:
  dbPath: /home/xx/mongodb/configs/data
  journal:
    enabled: true

systemLog:
  destination: file
  logAppend: true
  path: /home/xx/mongodb/configs/log/mongod.log

net:
  port: 13000
  bindIp: 0.0.0.0

processManagement:
  timeZoneInfo: /usr/share/zoneinfo

replication:
  replSetName: configRS
```
在三台机器的目录```~/mongodb/configs/```下均执行如下命令：
```
mongod -f mongod.conf --fork --configsvr
```
在其中任意一台上进入mongo shell
```
mongo --port 13000
```
将三台配置服务器级成复制集：
```
config = { _id: 'configRS', configsvr: true, members: [ {_id: 0, host: '192.168.0.130:13000'}, {_id: 1, host: '192.168.0.131:13000'}, {_id: 2, host: '192.168.0.132:13000'}, ] }

rs.initiate(config)
```
> 执行 ```rs.status()```查看是否成功

#### 二、完成rs0和rs1复制集服务器配置，在三台机器上均进入目录```~/mongodb/rs0/```下创建```mongod.conf```文件，写入如下内容：
```
storage:
  dbPath: /home/xx/mongodb/rs0/data
  journal:
    enabled: true

systemLog:
  destination: file
  logAppend: true
  path: /home/xx/mongodb/rs0/log/mongod.log

net:
  port: 11000
  bindIp: 0.0.0.0

processManagement:
  timeZoneInfo: /usr/share/zoneinfo

replication:
  replSetName: rs0
```
在三台服务器上的目录```~/mongodb/rs0/```下，均执行如下命令：
```
mongod -f mongod.conf --fork --shardsvr
```
> --shardsvr，在我们只是用复制集时，没有加这个选项，但是如果复制集是用来充当Shard用，就需要加上此参数  

在其中任意一台上进入mongo shell
```
mongo --port 11000
```
将三台服务器配置成复制集：
```
config = { _id: 'rs0', members: [ {_id: 0, host: '192.168.0.130:11000'}, {_id: 1, host: '192.168.0.131:11000'}, {_id: 2, host: '192.168.0.132:11000'}, ] }

rs.initiate(config)
```
> 执行```rs.status()```查看是否成功

重复以上步骤，配置rs1。
mongod.conf内容：
```
storage:
  dbPath: /home/xx/mongodb/rs1/data
  journal:
    enabled: true
#  engine:
#  mmapv1:
#  wiredTiger:

# where to write logging data.
systemLog:
  destination: file
  logAppend: true
  path: /home/xx/mongodb/rs1/log/mongod.log

# network interfaces
net:
  port: 12000
  bindIp: 0.0.0.0


# how the process runs
processManagement:
  timeZoneInfo: /usr/share/zoneinfo

#security:

#operationProfiling:

replication:
  replSetName: rs1

```
配置成复制集时的config：
```
config = { _id: 'rs1', members: [ {_id: 0, host: '192.168.0.130:12000'}, {_id: 1, host: '192.168.0.131:12000'}, {_id: 2, host: '192.168.0.132:12000'}, ] }
```
#### 三、完成mongos服务器配置
mongos服务器也打算配置三台
在三台服务器的```~/mongodb/mongos/```下，均创建文件```mongos.conf```，写入如下内容：
```
systemLog:
  destination: file
  logAppend: true
  path: /home/xx/mongodb/mongos/log/mongod.log
net:
  port: 14000
  bindIp: 0.0.0.0
processManagement:
  timeZoneInfo: /usr/share/zoneinfo
sharding:
    configDB: "configRS/192.168.0.130:13000,192.168.0.131:13000,192.168.0.132:13000"
```
> 其中configDB是我们之前配置的配置服务器的复制集，以复制集的名称开头，后面跟所有对应的IP:PORT。

在三台机器上的目录```~/mongodb/mongos/```下均执行命令：
```
mongos -f mongos.conf --fork
```
在任意一台机器上，进入mongo shell：
```
mongo --port 14000
```
执行增加shard命令：
```
sh.addShard('rs0/192.168.0.130:11000')
sh.addShard('rs1/192.168.0.130:12000')
```
> 现在两个Shard就配置成了集群模式  
> 可以执行命令```sh.status()```来查看状态。  
> 这里需要注意，在addShard时，只指定了一个服务器的IP，  
> 但是你执行```sh.status()```时会发现三台对应的IP:PORT就都有了  

#### 四、测试集群
连接三台中任意一台mongos
```
mongo --port 14000
```
创建测试数据：
```
use dealer
db.createCollection('goods')
sh.shardCollection('dealer.goods', {id: 'hashed'}, false)

let count = 0;
let goods = [];
for (let i = 0; i < 10000; i ++) {
    goods.push({
        id: i,
        name: 'goods-' + i,
    })
}
db.goods.insertMany(goods);
```
现在使用命令查看shard分布：
```
db.goods.getShardDistribution()
```