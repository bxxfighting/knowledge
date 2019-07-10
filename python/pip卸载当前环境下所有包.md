### 问题
现在有一个python环境，用pip安装过很多包，现在想把所有都清空  

### 解决办法
```
pip freeze | xargs pip uninstall -y
```
> -y: 是不用输入y确认  
