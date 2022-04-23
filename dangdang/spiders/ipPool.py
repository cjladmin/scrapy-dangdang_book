import scrapy
import requests
from ..items import IpPoolItem


class IppoolSpider(scrapy.Spider):
    name = 'ipPool'
    allowed_domains = ['89ip.cn']
    start_urls = ['https://www.89ip.cn/']

    def parse(self, response):
        for i in range(1, 30):
            url = response.url + f"index_{str(i)}.html"
            yield scrapy.Request(url=url, callback=self.get_ip_list)

    def get_ip_list(self, response):
        ip_list = response.xpath('//table//tr')
        # print(len(ip_list))
        for i in range(1, len(ip_list)):
            item = IpPoolItem()
            # 提取ip地址
            ip_address = ip_list[i].xpath(f'./td[1]/text()')[0]
            # 提取ip端口
            ip_port = ip_list[i].xpath(f'./td[2]/text()')[0]
            # 去除无用字符，并拼接为ip可用格式
            ip_msg = "http://" + ip_address.strip(" \t\n") + ":" + ip_port.strip(" \t\n")

            # 测试ip可用性
            if self.test_ip(ip_msg) is True:
                # 发给管道储存
                item['ip_address'] = ip_msg
                print(item)
                return item
        pass

    def test_ip(self, ip_msg):
        url = "http://www.baidu.com"
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
        }
        poxyz = {
            "http": ip_msg,
        }
        try:
            res = requests.get(url=url, headers=headers, proxies=poxyz, timeout=1)
            if res.status_code == 200:
                return True
        except Exception:
            return False
