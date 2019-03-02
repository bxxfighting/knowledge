### 问题:
自己控制gunicorn的启动和停止比较麻烦，  
所以在linux下很多程序的运行都交给了supervisor。  
因此，这里我们将gunicorn也使用supervisor来管理。  
### 解决办法:
在supervisor的配置文件(/etc/supervisor/supervisord.conf)中增加如下内容:  
```
[program:trace]
directory=/var/www/trace/
command=gunicorn application:app -c trace/gunicorn.conf
autostart=true
stdout_logfile=/var/log/supervisor/trace_out.log
stdout_logfile_maxbytes=10MB
stdout_logfile_backups=10
stderr_logfile=/var/log/supervisor/trace_err.log
stderr_logfile_maxbytes=10MB
stderr_logfile_backups=10
```
在配置完成后，通过执行```supervisorctl reload```来生效。  
但是我这里遇到了另一个问题: 我的gunicorn成功的启动了，但是在supervisorctl进入后，  
显示我的程序没有退出了。  
先展示一下出现问题时，我的gunicorn.conf文件内容:  
```
import os
import multiprocessing

CUR_DIR = os.path.dirname(os.path.dirname(__file__))

bind = "0.0.0.0:38987"
workers = multiprocessing.cpu_count() * 2 + 1
chdir = CUR_DIR
preload = True
daemon = True
```
这个问题的原因是，我的gunicorn自身的配置文件中指定以守护进程的方式启动，  
也就是```daemon = True```，因为守护进程的特性(不明白可以搜索一下)导致supervisor  
不能监测运行起来的程序。  
因此，这里改成```daemon = False```之后，再reload就正常了。  