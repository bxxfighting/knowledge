### 问题：

在linux系统下新创建用户

### 解决办法：

1. 创建xx用户

   ```
   sudo useradd hadoop -m -s /bin/bash
   ```

   > 在查看man手册里有介绍，
   >
   > -m是创建主目录，这里创建用户xx，那么主目录就是/home/xx。
   >
   > -s，后面加上使用的shell，就是指定默认使用的shell

2. 创建密码

   ```
   sudo passwd xx
   ```

3. 给xx用户指定权限

   ```
   sudo vim /etc/sudoers
   ```

   增加如下内容：

   ```
   xx ALL=(ALL:ALL) ALL
   ```

   > 现在新创建的用户就拥有了root权限

