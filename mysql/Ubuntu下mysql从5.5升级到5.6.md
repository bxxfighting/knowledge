#### 问题:
Ubuntu14.04下，开发环境的是mysql5.5，线上环境使用的是mysql5.6，因为是django项目，线上在使用migrate创建数据表时，DateTimeField会创建成datetime(6)，而mysql5.5是不支持datetime(6)这种类型的(只有datetime类型)，因此需要将开发环境的mysql升级到5.6
#### 解决办法:
[官网升级mysql文档](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#repo-qg-apt-upgrading)
1. 下载mysql-apt-config
    ```
    wget https://repo.mysql.com//mysql-apt-config_0.8.9-1_all.deb
    ```
    >我下载时是0.8.9这个版本，[根据你下载时最新版本下载](https://dev.mysql.com/downloads/repo/apt/)
2. 安装mysql-apt-config
    ```
    sudo dpkg -i mysql-apt-config_0.8.9-1_all.deb
    ```
    >在安装过程中，会让你选择要安装的mysql版本，我选择了mysql5.6，另外两个选项我都选了 **Enabled**。
3. 更新Ubuntu包信息
    ```
    sudo apt-get update
    ```
4. 安装mysql5.6
    ```
    sudo apt-get install mysql-server
    ```
    >这里官网上说直接执行上面的命令就可以了，但是我的不行，下面一直报需要一些依赖等等，而且提醒需要加上 **-f** 参数:
    ```
    sudo apt-get -f install mysql-server
    ```
    
#### 坑:
我在开发环境遇到的问题是要加-f，但是在测试环境升级后，运行不起来mysql，一直到下面这个错:
```
/usr/sbin/mysqld: Can't read dir of '/etc/mysql/mysql.conf.d/' (Errcode: 13 - Permission denied)
Fatal error in defaults handling. Program aborted
```
我查看了一下其它环境这个目录的权限从表现上看没有问题，而且我通过
```
chmod 777 mysql.conf.d -R
```
不管用
```
chown mysql:mysql mysql.conf.d -R
```
也不管用
最后，因为急着用，暂时将mysql.conf.d下文件内容复制到了my.cnf中，同时注释掉引用mysql.conf.d
```
[mysqld]
pid-file    = /var/run/mysqld/mysqld.pid
socket      = /var/run/mysqld/mysqld.sock
datadir     = /var/lib/mysql
log-error   = /var/log/mysql/error.log
# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0
!includedir /etc/mysql/conf.d/
# !includedir /etc/mysql/mysql.conf.d/
```
暂时这么解决@！