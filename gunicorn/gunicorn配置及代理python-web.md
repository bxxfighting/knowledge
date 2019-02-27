# 问题：
gunicorn配置及代理django及flask

# 解决办法：
```
import os
import multiprocessing

CUR_DIR = os.path.dirname(os.path.dirname(__file__))

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
chdir = CUR_DIR
preload = True
# 去掉daemon，因为要使用supervisor来管理
# daemon = True
```
> 上述为基础配置

启动django项目使用:
```
gunicorn demo.wsgi:application -c demo/gunicorn.py
```
启动flask项目使用:
```
gunicorn application:app -c demo/gunicorn.conf
```
> 其中application为当前目录下的文件名，里面有实例出的app

application.py
```
app = Flask('demo')
```
为了增加服务器的并发能力，我们可以将gunicorn配置成异步处理模块，这里需要用到gevent
```
pip install gevent
gunicorn demo.wsgi:application -k gevent -c demo/gunicorn.py
```
