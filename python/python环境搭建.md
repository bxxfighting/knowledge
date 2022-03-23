1. 下载pyenv
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```
> 详细见：
https://github.com/pyenv/pyenv#choosing-the-python-version

2. 配置pyenv路径
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
source ~/.bash_profile
```
3. 查看已经安装的python版本
```
pyenv versions
```
4. 查看可以安装的版本
```
pyenv install --list
```
5. 安装一些必要的库

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev
```
> 详细见：
https://github.com/pyenv/pyenv/wiki/Common-build-problems

6. 安装新的python版本
```
pyenv install 3.6.4
```
7. 切换python版本
```
pyenv global 3.6.4
```
> 到这里，我们就可以自由的切换不同的python版本了，但是还不能满足我们的需求，我们可能有时候在同一python版本下，可能会用到同一个库的不同版本，比如django1.8.6和django1.11.10，因此，还需要再安装pyenv-virtualenv

8. 安装pyenv-virtualenv
```
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```
> 详细见:
https://github.com/pyenv/pyenv-virtualenv

9. 配置pyenv-virtualenv
```
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile
```
10. 创建虚拟环境
```
pyenv virtualenv 3.6.4 py364dj186
```
> 我这里是创建一个python3.6.4,并且要安装django1.8.6的环境，或者这里起名可以用项目名称来代替，因为什么项目使用什么环境我们自己是知道的

11. 查看所有虚拟环境
```
pyenv virtualenvs
```
12. 激活虚拟环境并安装相应包
```
pyenv activate py364dj186
pip install django==1.8.6
```
13. 退出虚拟环境
```
pyenv deactivate
```

### 备注
如果在pyenv install时，下载python过慢，可以自己下载根据显示的那个链接自己下载。  
下载后，放到如下目录```.pyenv/cache/```下，cache如果不存在，需要自己创建出来。  

### 最新配置
#### MAC
.profile文件
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
.zshrc
```
source .profile
```

#### Ubuntu
.profile
```
source .bashrc

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
