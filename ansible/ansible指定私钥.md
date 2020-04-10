### 问题：
ansible不使用系统默认私钥，需要单独指定  
### 解决办法：
```
ansible-playbook --private-key ~/.ssh/id_rsa-ansible
```
> 运行时增加参数--private-key来指定使用的私钥位置