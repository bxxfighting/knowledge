### 问题
php项目配置nginx  

### 解决办法
```
server {
    server_name {{domain}};
    listen 80;
    root {{service_dir}}/{{xxx}};
    index index.php;
    set $yii_bootstrap "index.php";
    charset utf-8;

    add_header Cache-Control 'no-store, no-cache';

    access_log /mnt/log/nginx/{{domain}}-access.log;
    error_log /mnt/log/nginx/{{domain}}-error.log;

    location / {
        index index.php;
        if (!-e $request_filename){
        rewrite ^/(.*) /index.php last;
        add_header 'Access-Control-Allow-Headers' 'ua-limi';
        }
    }

    location ~ ^/(protected|framework|thems/\w+/views) {
        deny all;
    }

    location ~ \.(php|php5)?$ {
        fastcgi_split_path_info  ^(.+\.php)(.*)$;

        set $fsn /$yii_bootstrap;
        if (-f $document_root$fastcgi_script_name){
                set $fsn $fastcgi_script_name;
        }
        fastcgi_param  SCRIPT_FILENAME  $document_root$fsn;
        fastcgi_param  PATH_INFO        $fastcgi_path_info;
        fastcgi_param  PATH_TRANSLATED  $document_root$fsn;

        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        include        fastcgi.conf;
    }
}
```

> 其中domain为域名，service_dir为部署的根目录，xxx为目录下具体放置index.php的目录  
> log目录根据实际配置  
