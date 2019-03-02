# 问题：
mysql实现了双主互备后，如果我们同时使用两台服务器，那么，  
一台出问题后，需要将对应的应用服务器连接到另一台mysql上。  
我们如果统一连一台服务器，这台服务器挂了，需要我们手动切换成另一台服务器。  
现在还实现自动切换

# 解决办法：
使用keepalived来实现LVS负载均衡
下载：http://www.keepalived.org/download.html

解压  
./configure  
make  
make install  

192.168.31.82机器A：
```
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.31.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

vrrp_instance VI_1 {
    state MASTER
    interface enp0s3
    virtual_router_id 51
    priority 100
    advert_int 10
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.31.244
    }
}

virtual_server 192.168.31.244 3306 {
    delay_loop 6
    lb_algo rr
    lb_kind DR
    persistence_timeout 0
    protocol TCP
    real_server 192.168.31.82 3306 {
        weight 1
        TCP_CHECK {
            connect_timeout 10
            nb_get_retry 3
            delay_before_retry 3
            connect_port 3306
        }
    }
}
```
> global_defs中的内容我没有修改过，是默认的配置
> interface enp0s3为机器上的网卡名称(ifconfig)
> state MASTER设置为主，另一台设置为从


192.168.31.126机器B：
```
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.31.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}

vrrp_instance VI_1 {
    state BACKUP
    interface enp0s3
    virtual_router_id 51
    priority 100
    advert_int 10
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {
        192.168.31.244
    }
}
virtual_server 192.168.31.244 3306 {
    delay_loop 6
    lb_algo rr
    lb_kind DR
    persistence_timeout 0
    protocol TCP

    real_server 192.168.31.126 3306 {
        weight 1
        TCP_CHECK {
            connect_timeout 10
            nb_get_retry 3
            delay_before_retry 3
            connect_port 3306
        }
    }
}
```

A、B机器上启动：
```
sudo service keepalived start
```

通过命令：
```
ip a
```
查看网卡上的ip是否绑定成功

#### 遇到的问题
1. keepalived无法正常启动。  
原本我看到配置在```/usr/local/etc/keepalived/keepalived.conf```，  
但是实际运行时，读取的位置是```/etc/keepalived/keepalived.conf```。  

2. 虚拟出来的192.168.31.244这个IP无法ping通
通过命令```sudo service keepalived stop```关闭机器A上的keepalived，  
在机器B上使用```ip a```发现，```192.168.31.244```已经设置到了B机器上。  
但是外部机器无法ping通。ufw并未开启，说明不是这的问题。  
通过命令：
```
sudo iptables -nvL
```
发现原来192.168.31.244的进出都被DROP了
```
Chain INPUT (policy ACCEPT 12719 packets, 1447K bytes)
 pkts bytes target     prot opt in     out     source               destination
   10   600 DROP       all  --  *      *       0.0.0.0/0            192.168.31.244

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 12701 packets, 1435K bytes)
 pkts bytes target     prot opt in     out     source               destination
    8   672 DROP       all  --  *      *       192.168.31.244       0.0.0.0/0
```
最暴力的方法：
```
sudo iptables -F
```
允许所有的进出请求

> 这里有一个问题，在ip切换到新的机器上后，默认```iptables```对于这个IP又是DROP，  
> 需要允许才行。所以这里就出了问题，直接将keepalived配置中的```vrrp_strict```删除即可