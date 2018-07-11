### 问题：
如果使用docker来操作mysql
### 解决办法：
1. 获取mysql的docker镜像
```
sudo docker pull mysql:5.7
```
2. 运行mysql
```
sudo docker run --name test -p 3308:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7
```
> 运行mysql时，--name用指定运行起来的实例名称，-p后面是将本机的3308端口映射到实例的3306端口，MYSQL_ROOT_PASSWORD指定root用户密码，-d来指定后台运行，最后指定要运行的镜像及版本。

3. 连接到mysql
```
sudo docker exec -it test bash
mysql -uroot -p
```
> 执行上面第一条命令就会进入到运行刚才mysql实例的一个docker实例中，再执行第二条正常连接mysql的命令，就可以进行mysql操作了

4. 查看当前运行的docker实例
```
sudo docker ps
```
> 先回到我们本机的shell执行上面命令

5. 停止与运行
```
sudo docker stop test
sudo docker start test
```
> 执行上面两个命令可以停止和再次运行刚才的mysql实例，同时连接上发现数据仍然存在

6. 其他操作
> 执行```sudo docker stop test```后，再执行```sudo docker ps```是不能查看到test了，
> 因为此命令默认是查看运行的容器，执行```sudo docker ps -a```就可以查看所有容器了。
> ```sudo docker container ls -a```和```sudo docker ps -a```效果一样。
