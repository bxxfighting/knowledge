### 问题
如何获取django项目所以url，主要是在做url的权限控制时，方便一次性录入  

### 解决办法
```
from django.urls.resolvers import URLPattern
from django.urls.resolvers import URLResolver

from taiji.urls import urlpatterns

def get_all_urls():
    sub_urls = []
    for urlpattern in urlpatterns:
        sub_urls += find_sub_urls(urlpattern)
    # 这里我把所有url开头加上了斜线，如果没有这个需求可以不用
    urls = ['/' + sub_url for sub_url in sub_urls]
    return urls

def find_sub_urls(urlpattern):
    url = urlpattern.pattern.describe().replace('\'', '')
    # 如果是URLPattern，就说明到最后一层了，直接返回url就可以，但是需要返回列表结构 
    if isinstance(urlpattern, URLPattern):
        return [url]
    elif isinstance(urlpattern, URLResolver):
        sub_urls = []
        for p in urlpattern.url_patterns:
            sub_urls += find_sub_urls(p)
        urls = [url + sub_url for sub_url in sub_urls]
        return urls
```

> 这里taiji是我的django项目名称，需要根据自己的项目名称来修改  
> 最后的结果集是```['/api/v1/project/service/gitlab/tag/list/', '/api/v1/project/service/gitlab/branch/list/']```  
