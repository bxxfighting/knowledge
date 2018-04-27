### 问题:
git项目在commit时，增加flake8检查

### 解决办法:

1. 首先我们在使用git的一些操作之前想有一些自己的处理的话，都在写到git的hooks里，位置在
```.git/hooks/```，commit时候的处理都写在```.git/hooks/pre-commit```这个文件里

2. 安装pre-commit：  
命令: ```pip install pre-commit```  
官方网站: https://pre-commit.com/

3. 在项目下创建文件```.pre-commit-config.yaml```，并且到pre-commit的github地址去复制一份配置下来.  
pre-commit的github地址:
https://github.com/pre-commit/pre-commit/  
这个配置里面只保留flake8就可以了, 如下:
```
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v1.2.3
    hooks:
    -   id: flake8
```
4. 现在执行```pre-commit install```, 就会将相应的检查功能代码写入到```.git/hooks/pre-commit```中(如果文件不存在，在写入的时候会自动创建)

5. 现在就可以进行正常的git操作了，在commit执行的时候，如果代码格式有问题就会出现报错，修正后再add后commit

6. 如果了解flake8，想重新设置一些检查值可以切换到$HOME目录```cd ~```，查看目录下是否有```.config```这个隐藏目录，如果没有就创建```mkdir ~/.config```，然后在.config目录创建文件flake8, 里面增加如下内容:  
```
[flake8]
max-line-length=100
```
> 这里我只是配置了一个单行代码长度限制，默认是79, 我这里重新设置成100，  
> 这样单行代码就可以写到100了，如果需要其它配置修改，就需要查看flake8都有哪些可配置项了  
> flake8文档: http://flake8.pycqa.org/en/latest/
