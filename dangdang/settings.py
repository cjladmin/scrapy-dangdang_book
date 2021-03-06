# Scrapy settings for dangdang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dangdang'

SPIDER_MODULES = ['dangdang.spiders']
NEWSPIDER_MODULE = 'dangdang.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'

# 分布式相关配置：
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True
# REDIS_URL = 'redis://IP:6379'  # 将IP改为自己Redis数据库的地址

# 设置爬取间隔(s)
# DOWNLOAD_DELAY = 1

# 管道配置
ITEM_PIPELINES = {
   'dangdang.pipelines.DangdangPipeline': 301,
   'dangdang.pipelines.IpPoolPipelines': 300,
   # 当开启该管道，数据将会被存储到Redis数据库中
   # 'scrapy_redis.pipelines.RedisPipeline': 400,
}

# ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
   # 'dangdang.middlewares.DangdangDownloaderMiddleware': 543,
   'dangdang.middlewares.SeleniumMiddleware': 543,
   'dangdang.middlewares.ChangeMeMiddleware': 542,
}