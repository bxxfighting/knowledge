问题：
在创建订单时，其中有一个与mongo交互的操作，当天服务器CPU利用率被mongo占很高。
解决办法：
1. 查看当前执行操作
> 因为我们这个属于突然出现的情况，所以肯定要从当前执行的操作进行查找问题
```
db.currentOp()
```
来查看当前正在执行的操作有没有问题
```
> db.currentOp()
{
    "inprog" : [
        {
            "desc" : "conn264",
            "threadId" : "139665256978176",
            "connectionId" : 264,
            "client" : "127.0.0.1:39024",
            "appName" : "MongoDB Shell",
            "active" : true,
            "opid" : 9539571,
            "secs_running" : 0,
            "microsecs_running" : NumberLong(12),
            "op" : "command",
            "ns" : "admin.$cmd",
            "query" : {
                "currentOp" : 1
            },
            "numYields" : 0,
            "locks" : {

            },
            "waitingForLock" : false,
            "lockStats" : {

            }
        }
    ],
    "ok" : 1
}
```
根据其中的secs_running和secs_running来看，是否正在执行的操作有没有时间长的，如果有，可以看当前执行的操作是否可以中止，如果可以，执行db.killOp(opid)终止这个操作。
> 我们的情况到现在基本已经解决了，因为我们是另一个程序员在跑一个处理商品的脚本，并且没有索引，在输出的结果中有一个为COLLSCAN值，这就是冷扫描也就是全表扫描，这是非常耗时的，而且原本可以批处理的，最后还是一个大循环。

2. 使用db.system.profile来查看其它慢操作
> 如果mongo的CPU占用率一直很高，那么往往是因为本身使用上有问题，可能未建议相关的索引
```
> db.getProfilingStatus()
{ "was" : 0, "slowms" : 100 }
```
> was为0说明没有开启

```
> db.setProfilingLevel(1)
{ "was" : 1, "slowms" : 100, "ok" : 1 }
```
> db.setProfilingLevel有两个参数，
> 第一个是级别：0，1，2
> 第二个是时间
> 0：关闭
> 1: 开启，并且执行时间大于第二个时间设置值的记录
> 2: 开启，并且记录所有记录

```
db.system.profile.find().pretty()
```
> 这里还是一样，根据输出的结果去，找耗时多的，或者有COLLSCAN值的，然后根据自己的实际情况来处理就可以了
