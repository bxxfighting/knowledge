### 问题：

我们有一个model是Order，其中有一个字段是create_time，也就是DateTimeField类型，但是现在想要按天来聚合一下，看看每天有多少订单。

### 解决办法：

```
from django.db import connection
from order.modes import Order
from django.db.models import Count

select = {'day': connection.ops.date_trunc_sql('day', 'create_time')}
Order.objects.extra(select=select).values('day').annotate(count=Count('id'))
```

> 上面的查询语句转化成sql大概是这样的
>
> ```
> select count(id), DATE_FORMAT(deal_time, '%Y-%m-%d') days from order_order group by days;
> ```

### 坑：

> 在django的settings.py文件中，有一个变量
>
> ```
> USE_TZ=True
> TIME_ZONE = 'Asia/Shanghai'
> ```
>
> 如果USE_TZ设置成了True，那么django的ORM就会把时间转成UTC时间后存入mysql中。
>
> 在这种情况下使用上面的聚合方法就会出现问题。
>
> 举个例子：
>
> 我们的2017-10-02这一天的时间的UTC时间范围是：2017-10-01 16:00:00  — 2017-10-02 16:00:00
>
> 在使用上面的聚合时，2017-10-02这一天会被聚合成两天(2017-10-01,2017-10-02)
>
> 因此，只有在mysql中存的是你本地时间时，才可以使用此方法。
>
> 在django中可以通过创建项目后，把USE_TZ设置成False来完成此目的。
>
> 如果已经是咱们项目这种结果了，那么可以通过原始SQL方式进行聚合：
>
> ```
> select count(id), DATE_FORMAT(DATE_ADD(deal_time, interval 8 hour), '%Y-%m-%d') days from order_order group by days;
> ```
>
> 转成django:
>
> ```
> from django.db import connection
>
> cursor = connection.cursor()
> cursor.execute("select count(id), DATE_FORMAT(DATE_ADD(deal_time, interval 8 hour), '%Y-%m-%d') days from order_order group by days")
> rows = cursor.fetchall()
> ```
>
> 这样就可以取出聚合好的数据了，使用rows值来进行其它业务处理。
>
> 如果不使用原始SQL的方式，其实也可以采用最上面的extra，代码如下：
>
> ```
> from django.db import connection
> from order.modes import Order
> from django.db.models import Count
>
> select = {'day': connection.ops.date_trunc_sql('day', 'DATE_ADD(deal_time, interval 8 hour)')}
> Order.objects.extra(select=select).values('day').annotate(count=Count('id'))
> ```
>
> 这样就可以继续按django的聚合方式来进行了。这里就是把
>
> ```
> 'create_time'
> ```
>
> 换成了：
>
> ```
> 'DATE_ADD(deal_time, interval 8 hour)'
> ```
>
> 