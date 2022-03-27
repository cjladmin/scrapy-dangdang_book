# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # 大分类标题
    big_category_title = scrapy.Field()
    # 大分类链接
    big_category_link = scrapy.Field()
    # 小分类标题
    smell_category_title = scrapy.Field()
    # 小分类链接
    smell_category_link = scrapy.Field()

    # 书名
    book_name = scrapy.Field()
    # 作者
    book_author = scrapy.Field()
    # 日期
    book_date = scrapy.Field()
    # 出版社
    book_press = scrapy.Field()
    # 书价
    book_price = scrapy.Field()
    # 链接
    book_link = scrapy.Field()
    pass


class IpPoolItem(scrapy.Item):
    # IP地址
    ip_address = scrapy.Field()
    pass
