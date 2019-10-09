### 问题
我现在想对nginx日志进行一下分析，可以进行可视化的展示  
### 解决办法
我的nginx日志文件名access.log，记录格式如下：
```
288.188.388.188 121.121.131.131 [24/Sep/2019:00:01:01 +0800] baidu.com 177.177.177.121 "POST /gogo HTTP/1.1" 200 1554 "-" 127.0.0.1:5000 200 "okhttp/4.0.1" 0.470 0.469
```
使用goaccess
先写一个goaccess的配置文件，goaccess.conf，内容如下：
```
time-format %H:%M:%S
date-format %d/%b/%Y
log-format %^ %h [%d:%t %^] %^ %^ "%r" %s %b "%^" %^ %^ "%u" %T %^
hour-spec min
```
> 先配置time-format和date-format的格式，这是必须要的，然后根据你的nginx日志  
> 配置log-format格式，其中%d代表你上面配置的date-format，%t代表time-format，  
> %^：忽略此值  
> %h：客户端IP地址  
> hour-spec min：指定将一小时划分成每十分钟一个统计数据  
> [具体各个参数说明](https://goaccess.io/man)

之后生成html
```
goaccess access.log -o report.html -p goaccess.conf
```
> -o：指定生成html文件名  
> -p: 指定配置文件  

如果有多个文件可以执行如下命令：
```
cat access-* | goaccess -o report.html -p goaccess.conf
```

### 重要提示
我在安装goaccess时，是在mac系统上进行的，安装完成后，在使用时，  
总是提示日期格式和%d不匹配。后来发现，这个goaccess是语言是根据当前系统决定的，  
而我的系统是中文，然后nginx日志中的月份是用的英文缩写，我把英文缩写改成中文就行了，  
比如这里Sep我全部替换成九月就可以了。但是这样太蠢了，我就把系统的语言修改成了英文。  
