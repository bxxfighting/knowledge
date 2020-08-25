### 问题
在配置upstream时参数都是什么含义  


### 解决办法

```
upstream buxingxing.com {
    server 127.0.0.1:8001 weight=10 max_fails=1 fail_timeout=30;
    server 127.0.0.1:8002 weight=10 max_fails=1 fail_timeout=30;
    server 127.0.0.1:8003 weight=10 max_fails=1 fail_timeout=30;
}
```
当有请求时，在fail_timeout时间内，出现max_fails次失败，就标记此server不可用，此标记有效期为fail_timeout，  
当过了fail_timeout时长后，再次请求判断是否可用  
