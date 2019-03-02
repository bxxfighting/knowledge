# 问题：
将python web应用docker部署

# 解决办法：
以django为例，在项目的根目录增加Dockerfile文件，现在目录结构是这样的：
```
.:
Dockerfile  demo  manage.py  requirements.txt  start.sh

./demo:
__init__.py  gunicorn.py  settings.py  urls.py  views.py  wsgi.py
```
其中Dockerfile内容如下：
```
FROM python:3.6.8
MAINTAINER xx 305526954@qq.com

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
RUN chmod 777 /code/start.sh
EXPOSE 8000
CMD ["/code/start.sh"]
```

start.sh内容如下：
```
#!/bin/bash

gunicorn demo.wsgi:application -c demo/gunicorn.py
```

执行命令创建docker镜像：
```
sudo docker build -t xx/demo .
```
> xx/demo是我自己指定的镜像名称

创建并运行容器：
```
sudo docker run -d -p 8000:8000 --name demo xx/demo
```
> 这里需要记住，容器用-d命令守护进程运行。
> 而在demo/gunicorn.py中要将daemon=True去掉，
> 不要以守护进程运行，并且gunicorn.py中绑定的IP要用0.0.0.0

gunicorn.py示例：
```
import os
import multiprocessing

CUR_DIR = os.path.dirname(os.path.dirname(__file__))

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
chdir = CUR_DIR
preload = True
```