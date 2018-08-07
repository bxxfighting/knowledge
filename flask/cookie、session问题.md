### 问题:
flask中设置session和cookie问题，  
1. 设置```REMEMBER_COOKIE_DURATION=datetime.timedelta(hours=2)```但是在cookie中并没有生效。  
2. 设置```REMEMBER_COOKIE_DOMAIN = '.buxingxing.com'```在本地使用时没有生效  
3. 设置```PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=2)```但是在cookie中没有生效
### 解决办法:
1. 设置```REMEMBER_COOKIE_DURATION```，需要在调用```login_user```时需要传入参数```remember=True```
2. 设置```REMEMBER_COOKIE_DOMAIN```，主要是为了cookie跨域使用，设置成根域名，这样所有子域名下可以共用cookie，  
但是，本地使用的是localhost或者127.0.0.1，所以cookie因为域名不匹配所以设置不上。
3. 设置```PERMANENT_SESSION_LIFETIME```后，默认设置上的cookie是在浏览器退出后删除，如果想要按此时间来过期，  
则应该在调用请求中设置```session.permanent = True```（可以在统一的request处理方法中设置）
