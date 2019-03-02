# 问题：
mongodb搭建高可用

# 解决办法：

192.168.0.130机器A:
有目录如下：
```
/home/xx/mongodb/rs0
```
rs0下创建目录data、log，以及配置文件mongod.conf
mongod.conf内容如下：
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
> 这里的配置主要是从/etc/mongod.conf中复制过来的，  
> 修改了dbPath、log path、bindIp、port、replSetName  

192.168.0.131机器B:
创建同A机器一样的目录结构，配置文件内容一致

192.168.0.132机器C:
创建同A机器一样的目录结构，配置文件内容一致

三台机器上都在目录rs0下执行：
```
mongod --config mongod.conf --fork
```
> 建议第一次执行时，不加--fork，这样如果有错误方便查看  
> 如果可以正常运行，再关闭后加上--fork  

A机器上连接进入mongo的shell：
```
mongo --port 11000
```
执行如下命令：
```
config = { _id: "rs0", members: [{_id: 0, host: "192.168.0.130:11000"}]}
rs.initiate(config)
rs.add("192.168.0.131:11000")
rs.add("192.168.0.132:11000")
```
> 这里就已经配置上了复制集模式   
> 必须提供config，不能直接rs.initiate()，否则可能导致增加其它结点时，一直处于STARTUP状态  
> members必须要有一个元素，这里是本机的服务，而且_id也必须提供，host中不能使用localhost  
> 之后使用rs.add增加了B和C上的mongo服务。也可以在config的members中增加  

查看复制集配置：
```
rs.conf()
```
查看复制集状态：
```
rs.status()
```
> 这里"stateStr"应该为"PRIMARY"和"SECONDARY"，如果一直处在STARTUP，就需要查找问题  

默认进入shell后，db就代表是test应该。现在在test上做测试
A机器：
```
use test
db.goods.insert({'name': '香烟')
db.goods.find()
```
然后在机器B上：
```
use test
rs.slaveOk(true)
db.goods.find()
```
> 因为默认是读写都从PRIMARY节点操作的，现在要在SECONDARY上读，需要先执行rs.slavaOk(true)  

参考资料：https://docs.mongodb.com/manual/reference/replica-configuration/
