### 问题:
如果使用nginx进行负载均衡，当部署服务机器前应该使部署的机器down，然后部署完成后，再up  
正常这种操作在我想来要通过修改upstream内容，然后nginx -s reload才可以  
但是如果如果一个nginx集群，负载了很多服务，当部署一个服务时，就reload了所有，  
并且如果多台机器部署，一次部署才可以多次reload  


# 解决办法:
通过安装openresty，使用lua控制后端服务器的down/up  

详细内容参考[openresty-upstream-demo](https://github.com/bxxfighting/openresty-upstream-demo)
