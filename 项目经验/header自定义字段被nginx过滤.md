### 问题：
移动端需要传设备类型(device_typ)和版本信息(version)给服务端，使用http的header来自定义字段实现，
但是服务端只能收到version字段，不能收到device_typ

### 解决办法:
这是因为nginx服务器默认是过滤掉带有下划线的header字段的，所以device_typ被过滤掉了。  
因此需要将device_typ写成device-typ来传。  
如果不修改字段格式，也可以在nginx上配置支持下划线字段，  
但是，开启支持的效果是nginx帮你把下划线转成了中横线而已。

所以最好还是移动端将字段直接修改成device-typ