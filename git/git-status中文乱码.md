# 问题：
在执行git status时，中文显示不正确
```
"\345\255\227\345\205\270\346\216\222\345\272\217.md"
```
# 解决办法：
```
git config --global core.quotepath false
```
或者在自己的项目下的```.git/conf```中的core字段下增加```quotepath = false```
.git/conf
```
[core]
    quotepath = false
```
