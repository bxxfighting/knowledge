### 问题：

一台笔记本安装了Ubuntu16.04 Server版系统，只想用这个电脑当服务器，用别的电脑远程SSH连接使用，但是合上笔记本就睡眠，所以需要设置上，合上不睡眠。

### 解决办法：

> 1. 打开/etc/systemd/logind.conf文件 
>
> 2. 找到这句#HandleLidSwitch=suspend 
>
> 3. 改成HandleLidSwitch=ignore 
>

[参考链接](https://linux.cn/article-2485-1.html)