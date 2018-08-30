### 问题:
在我们公司当前使用alembic时，不检查字段的类型变化

### 解决办法:

在alembic相对应目录的env.py文件中  
```context.configure```的参数传入```compare_type=True```

> 官方文档:  
> http://alembic.zzzcomputing.com/en/latest/autogenerate.html#comparing-and-rendering-types
