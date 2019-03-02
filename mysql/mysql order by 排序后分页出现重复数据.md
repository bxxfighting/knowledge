### 问题
有一张表record，里面有一个字段是status表现记录的状态，现在根据status进行排序:
```
select * from record order by status desc limit 0,20;
select * from record order by status desc limit 20,20;
```
发现两个分页的集合中有重复数据出现。

### 解决办法
造成这个现象的原因是因为status本身是一个有很多重复值的字段，当使用该字段排序并使用了Limit时，同值的记录排序是不定的。所以在分页的时候就出现了问题。
mysql官方文档中有详情的一个例子: 
<html>
<a href="https://dev.mysql.com/doc/refman/5.7/en/limit-optimization.html" target="_blank">mysql官方文档</a>
</html>

那么现在我暂时使用的解决办法就是:
```
select * from record order by status desc, id desc limit 0,20;
select * from record order by status desc, id desc limit 20,20;
```
在排序后面加上同时使用id排序，因为id是唯一的，就不会出现此问题。