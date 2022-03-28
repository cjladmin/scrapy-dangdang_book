# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
import json

# MongoDB地址
mongo_address = '127.0.0.1'


# 保存到MongoDB数据库
class DangdangPipeline:
    def open_spider(self, spider):
        if spider.name == "book":
            # 建立和MongoDB的链接
            self.client = MongoClient(mongo_address, 27017)
            # 指定链接库
            self.db = self.client['dangdang']
            # 指定库集合
            self.col = self.db['book_rank']

    def process_item(self, item, spider):
        if spider.name == "book":
            data = dict(item)
            # 展示数据
            print(data)
            # 写入数据
            self.col.insert(data)
            return item

    def close_spider(self, spider):
        if spider.name == "book":
            # 断开连接
            self.client.close()


# 创建IP池
class IpPoolPipelines(object):
    def open_spider(self, spider):
        if spider.name == "ipPool":
            self.ip = open("ip_pool.json", 'w')

    def process_item(self, item, spider):
        if spider.name == "ipPool":
            dict_data = dict(item)
            data = json.dumps(dict_data, indent=1, ensure_ascii=False) + ","
            self.ip.write(data)
            return item

    def close_spider(self, spider):
        if spider.name == "ipPool":
            self.ip.close()
