### 问题：如何安装rabbitmq
在使用celery配置broker时，官方推荐使用rabbitmq，因此，就需要安装rabbitmq

### 解决办法:
我们使用docker来安装  
1. 下载rabbitmq  
```docker pull rabbitmq:3.7.8```  
2. 运行  
```docker run --name rabbitmq -p 5672:5672 -p 15672:15672 -d rabbitmq:3.7.8```  
3. 进入新运行的rabbitmq容器  
```docker exec -it rabbitmq bash```  
4. 启用网页管理  
```rabbitmq-plugins enable rabbitmq_management```  
5. 增加管理用户并设置角色  
```rabbitmqctl add_user xx xx```  
```rabbitmqctl set_user_tags xx administrator```  

> 5672端口为客户端连接端口，  
> 15672为网页管理连接端口  
> 默认用户为guest密码guest，  
> 可以通过第五步增加新的用户  
> 删除用户: ```rabbitmqctl delete_user xx```  
> 更改密码: ```rabbitmqctl change_password guest newpassword```  
> 用户列表: ```rabbitmqctl list_users```  
> 管理页面访问: http://127.0.0.1:15672