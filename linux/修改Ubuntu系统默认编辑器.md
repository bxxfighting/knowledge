### 问题：

在linux系统下，使用git等版本控制器时，输入commit时会使用系统默认编辑器，一般是nano，但我们平时一般都是用vim。

### 解决办法：

```
git config --global core.editor vim
```

> 这样就修改了git的默认编辑器

如果要修改系统的默认编辑器，则执行如下命令:

```
echo "export EDITOR=/usr/bin/vim" >> ~/.bashrc
```