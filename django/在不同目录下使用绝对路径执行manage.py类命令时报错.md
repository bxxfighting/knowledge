### 问题：
在项目中使用了Sentry，需要在settings中配置内容，如下：
```
RAVEN_CONFIG = {
    'dsn': 'http://.......'
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}
```
在网上搜索配置时，有几篇是这样给出的。照些配置上，看着好像没有问题，项目也正常运行，但是这里出现了一个坑。
比如，我们有一些定时任务是用crontab来运行的，内容如下：
```
0 2 * * * python /home/buxingxing/gogo/manage.py gen_name
```
如果按上面的配置过后，这个crontab就不能正常运行了，会报类似的错：
```
raven.exceptions.InvalidGitRepository: Cannot identify HEAD for git repository at
```
### 解决办法：
刚开始有这个报错的时候，我们以为是crontab写错了，就把它修改成下面这样:
```
0 2 * * * cd /home/buxingxing/gogo/; python manage.py gen_name
```
先进入项目目录后，再执行。这样看似解决了问题，其实不是正确的办法。
出现这个问题的主要原因是用了```os.pardir```，这是一个相对路径的表示方法，就导致你在不同目录下执行，```os.pardir```实际指向的路径是不同的（虽然看着都是```..```）  
##### 这里应该配置成这样：
```
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RAVEN_CONFIG = {
    'dsn': 'http://.......'
    'release': raven.fetch_git_sha(BASE_DIR),
}
```
一般在django项目中肯定都会设置一个BASE_DIR（不管叫什么名字），应该都使用这个来配置其它有关路径的参数