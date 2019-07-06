### 问题
在ubuntu下，安装完了docker后，往往需要sudo来执行docker命令  

### 解决办法
将当前用户加入用docker用户组中  
默认在安装docker的时候，会创建一个名为docker的组  
```
sudo usermod -aG docker xx
```
> xx为我的用户名  
退出，再重新进入shell，就可以了
