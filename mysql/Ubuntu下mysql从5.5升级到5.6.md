#### 问题:
Ubuntu14.04下，开发环境的是mysql5.5，线上环境使用的是mysql5.6，因为是django项目，线上在使用migrate创建数据表时，DateTimeField会创建成datetime(6)，而mysql5.5是不支持datetime(6)这种类型的(只有datetime类型)，因此需要将开发环境的mysql升级到5.6
#### 解决办法:
1. 下载mysql-apt-config  
    ```
    wget https://repo.mysql.com//mysql-apt-config_0.8.9-1_all.deb
    ```
    > 我下载时是0.8.9这个版本，根据你下载时最新版本下载
2. 安装mysql-apt-config  
    ```
    sudo dpkg -i mysql-apt-config_0.8.9-1_all.deb
    ```
    > 在安装过程中，会让你选择要安装的mysql版本，我选择了mysql5.6，另外两个选项我都选了 **Enabled**。
3. 更新Ubuntu包信息  
    ```
    sudo apt-get update
    ```
4. 安装mysql5.6  
    ```
    sudo apt-get install mysql-server
    ```
    > 这里官网上说直接执行上面的命令就可以了，但是我的不行，下面一直报需要一些依赖等等，而且提醒需要加上 **-f** 参数:
    ```
    sudo apt-get -f install mysql-server
    ```

[官网升级mysql文档](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/#repo-qg-apt-upgrading)