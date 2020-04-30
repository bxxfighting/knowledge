### 问题：
使用ansible git模块拉取代码时，冲突如何解决  

### 解决办法：
1. 首先在参数中增加```force: yes```，这样本地修改都会被清除，执行```git reset --hard HEAD```  
2. 在ansible中并未执行git pull，而是分开，先执行了git fetch  
3. 如果指定的version为分支，则先执行```git checkout --force version```，再执行```git reset --hard origin/version```  
4. 如果指定的version为tag号或commit号，则直接执行```git checkout --force version```  
