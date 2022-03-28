## <center>✨获取当当图书每天的实时畅销榜✨</center>
 - 当当图书畅销榜：[http://bang.dangdang.com/books/bestsellers/](http://bang.dangdang.com/books/bestsellers/)
 
 - 爬取畅销榜所有分类的TOP500图书信息，包含：
    - 图书名
    - 图书作者
    - 图书价格
    - 图书出版社
    - 图书详情链接

### 相关个人配置：
```
***一般配置***
文件：pipelines.py
    将mongo_address更改为自己MongoDB的地址，不更改默认为本地
文件：middlewares.py
    找到`proxys`，将ip_pool.json爬取到的免费可用ip代理地址，全部复制到proxys列表内
    如果自己有私人ip代理，则配置如下：
        {
            'ip_address': 'ip地址', 'user_passwd': 'user:passwd'
        }
***分布式配置***
文件：settings.py
    启用文件中被注释掉的“分布式相关配置”：
        DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
        SCHEDULER = "scrapy_redis.scheduler.Scheduler"
        SCHEDULER_PERSIST = True
        REDIS_URL = 'redis://IP:6379'
    启用'ITEM_PIPELINES'中的分布式管道
    选择性启用'DOWNLOAD_DELAY'，启用后可限制爬虫频率
```
    
### 运行环境及步骤：
 - 运行环境依赖模块：
```
scrapy
pymongo | redis
selenium
```
 - 运行步骤：
    1. 运行`ipPool`，指令`scrapy crawl ipPool`，从而提取可用的免费ip代理
    2. 配置相关文件后，运行`book`，指令`scrapy crawl book`，启动爬虫(需要有MongoDB数据库)
        - 或者也可通过修改`settings`文件，从而运行分布式爬虫，指令`scrapy runspider redis_book.py`，启动爬虫(需要有Redis数据库)