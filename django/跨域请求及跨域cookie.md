### 问题：

在项目中官网和我们App的域名buxingxing.com不一样，但是现在官网还在通过http请求到App的域名下的接口请求数据，这时就产生了跨域请求。

### 解决办法：
使用了第三方库:  
https://github.com/ottoyiu/django-cors-headers.git

在App项目中，settings.py文件中加入如下内容：

```
CORS_ORIGIN_WHITELIST = (
    'money.buxingxing.com',
    'water.buxingxing.com',
    'bunny.com',
)
```

其中，'money.buxingxing.com'、'water.buxingxing.com'、'bunny.com'就是那些想跨域请求'buxingxing.com'下接口的域名。（可以看出来，不管是二级域名还是不相关的其它域名都可以）

### 延伸：

比如，'money.buxingxing.com'是一个纯web前端项目使用的域名，所有其它接口都是调用'water.buxingxing.com'的接口完成，而且还包括登录接口，而登录使用了django的cookie，这时候登录生成的cookie是不能被'money.buxingxing.com'使用的。这里需要一些设置。

1. 首先前端请求时需要设置withCredentials为true
2. 然后在settings.py中增加CORS_COOKIES_DOMIAN = 'buxingxing.com'，在上面的CORS_ORIGIN_WHITELIST也一定要设置好。
3. 在settings.py中增加CORS_ALLOW_CREDENTIALS = True，这里和1相似，也就是服务器端和前端都要设置上才可以。

这里就实现了，'money.buxingxing.com'调用'water.buxingxing.com'的登录接口，同时可以使用登录生成的cookie。

