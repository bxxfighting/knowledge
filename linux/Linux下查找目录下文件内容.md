### 问题：

在一个目录下有很多文件，我们需要查找某一个词出现在哪个文件里，比如，在哪个文件中有”hello world“这句话

### 解决办法：

使用如下命令：

```
find . | xargs grep "hello world" -n
```

同时我们也可以指定我们要从哪些文件中搜索，比如我们只搜索c语言的程序文件，也就是后缀带有".c"的文件，命令如下：

```
find . -name "*.c" | xargs grep "hello world" -n
```

### 延伸：

如果要删除所有某一后缀名的文件，比如python生成的.pyc文件

```
find . -name "*.pyc" | xargs rm
```