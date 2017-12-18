### 问题：

在linux系统下使用vim来编程时，Ctrl键是经常使用的一个功能键，但是按起来不方便，因此需要改键，

将Caps Lock（大小写切换键）和Ctrl换位置。

### 解决办法：

```
setxkbmap -option ctrl:swapcaps
```

> 这个命令在终端执行就可以交换了，但是重启系统后失效，需要再次执行。因此需要写到文件中。

在/etc/bash.bashrc最后增加这句话，重启后依然生效

```
setxkbmap -option ctrl:swapcaps
```