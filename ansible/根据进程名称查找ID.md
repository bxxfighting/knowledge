### 问题：
现在有进程名称，想要查找进程ID  
### 解决办法：
```
- name: "获取当前服务PID"
  shell:
    cmd: "ps aux | awk '{print $2 \" \" $11}' | grep -E \"(\\d+)? ./{{service_name}}\" | grep -v grep | awk '{print $1}'"
  register: pid_result
```

> 先截取ps aux中的pid及进程名称字段，再使用数字 + 空格 + 进程名称的方式来精确