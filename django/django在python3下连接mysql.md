# 问题：
django使用python3后连接Mysql问题

# 解决办法：
安装 pymysql
```
pip install pymysql
```
同时在和settings.py同级目录下的__init__.py文件中加入:
```
import pymysql

pymsql.install_as_MySQLdb()
```
