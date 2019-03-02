### 问题：
App设定一个账号同时只能一个设备登录，在登录时使用的是Django的TimestampSigner用用户id来生成sign值设置session，但是当多个设备在同时登录时，因为id和时间都是相同的，所以生成了相同的sign值，导致多个设备同时登录Bug。

### 解决办法：
1. 在现在基础上，判断生成的sign是否已经存在，如果有，重新生成
2. 修改生成sign值方法，不用TimestampSign，使用uuid