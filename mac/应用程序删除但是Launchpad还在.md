### 问题:
在应用程序中删除了某一个应用，但是在Launchpad中还能看到，也不能删除

### 解决办法:
```
defaults write com.apple.dock ResetLaunchPad -bool true
killall Dock
```
> 命令端执行这两条命令即可  
