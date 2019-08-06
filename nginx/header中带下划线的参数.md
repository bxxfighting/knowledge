### 问题
在api的权限验证中，使用了token认证，即在请求的header中增加字段auth_token，  
但是服务端程序无法在header中取到此参数。  

### 解决办法
因为请求通过nginx转发，而nginx默认会忽略掉带有下划线的字段。  
因此，可以将auth_token，修改成auth-token。  
或者在nginx中增加配置：  
```
http {
    ...
    underscores_in_headers on;
    ...
}
```
> 其实我觉得最好还是将下划线改成中划线，这样减少对nginx的依赖  

[官方参考资料](http://nginx.org/en/docs/http/ngx_http_core_module.html#underscores_in_headers)

### 延伸
这里有一个有意思的地方，如果你使用的是django框架了，django会将所有header字符都转大写  
并且将中划线转成下划线，再前面增加HTTP_前缀，然后存放在request.META中，比如获取我们的token如下：  
```
request.META['HTTP_AUTH_TOKEN']
```
