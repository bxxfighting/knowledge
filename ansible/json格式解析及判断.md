### 问题：
通过接口获取json格式内容，并对返回内容进行判断  

> 来由，主要是因为通过nacos接口获取当前实例列表，进而判断当前机器是否此实例列表中  
> 文档：https://nacos.io/zh-cn/docs/open-api.html  


### 解决办法：
##### 数据：
```
{
    hosts: [
        {
            "name": "xx",
            "ip": "172.16.22.23",
            "port": "29999",
        },
        {
            "ip": "192.168.22.23",
            "port": "19999",
        },
    ]
}
```
##### ansible-playbook：
```
---
- hosts: all
  remote_user: root
  gather_facts: true
  vars:
    request_url: "http://json.com"
  tasks:
  - name:
    uri:
      url: "{{ request_url }}"
      return_content: yes
      body_format: json
    register: response
    until: "'172.16.16.18' in response.content | from_json | json_query('hosts[*].ip')"
    retries: 10
    delay: 2
```
> 此功能主要是用于，在重启服务后，通过接口判断，此服务是否已成功注册到nacos服务列表中  
> 重试10次，每次间隔2秒, 实际使用时，将172.16.16.18替换成当前机器IP：ansible_facts['default_ipv4']['address']  
