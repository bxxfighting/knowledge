### 问题：

最近在安装完Ubuntu系统后，然后在用apt install总是会警告如下：
```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LC_CTYPE = "zh_CN.UTF-8",
	LANG = "en_US.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to a fallback locale ("en_US.UTF-8").
```

### 解决办法：

执行如下命令：
```
sudo apt install locales-all
```
