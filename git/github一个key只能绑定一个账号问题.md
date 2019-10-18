### 问题
我有两个github账户，一个是个人的，一个是公司使用的，  
我电脑上生成的ssh key已经设置给了个人账号，再想设置给公司账号时，github是不允许的。  

### 解决办法
首先再生成一个ssh key，需要指定生成位置，不要覆盖原来的。  
然后配置.ssh/config：
```
Host companygithub
    Hostname github.com
    User bxx
    IdentityFile ~/.ssh/pem/id_rsa
    IdentitiesOnly yes
```
> 以上配置就是命令一个Host代表公司的github，  
> 这里的User其实无所谓了，很多人说设置成github的账户名，我感觉不用  
> IdentityFile就是指定新生成的key的位置  

以上配置完成后，就可以通过如下途径操作：
```
# 个人账户的代码还是通过原来的命令，比如：
git clone git@github.com:person/xxxx.git

# 公司账户的代码通过如下命令：
git clone git@companygithub:company/xxxx.git
```

这里有一点一定要注意，如果你之前已经通过一个key设置后删除的方式操作过两个库了，  
那么你使用新key的库就需要更改remote了。执行如下命令查看：
```
git remote -v
```
正常来说，如果是通过上面配置后，新clone下来的代码，这个显示会是类似这样：  
```
origin	git@companygithub:company/xxxx.git (fetch)
origin	git@companygithub:company/xxxx.git (push)
```
如果之前已经clone过了，要么重新clone，要么修改一个origin  
