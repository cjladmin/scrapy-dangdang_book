import scrapy
from ..items import DangdangItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/']

    def parse(self, response):
        # 获取大标题的节点列表
        big_node_list = response.xpath('//*[@id="sortRanking"]/div/a')
        # print(len(big_node_list))
        for big_node in big_node_list:
            temp = {}
            # 大分类名称
            big_category_title = big_node.xpath('./text()').extract_first()
            # 大分类链接
            big_category_link = big_node.xpath('./@href').extract_first()
            temp['big_category_title'] = big_category_title
            temp['big_category_link'] = big_category_link
            # 点击大标签链接
            yield scrapy.Request(url=big_category_link, callback=self.get_smell_node_list, meta=temp)
            break

    # 模拟点击大分类链接，从而获取小分类
    def get_smell_node_list(self, response):
        # 获取小标题的节点列表
        smell_node_ul_list = response.xpath('//*[@id="sortRanking"]/ul')
        # print(len(smell_node_ul_list))
        for smell_node_ul in smell_node_ul_list:
            smell_node_li_list = smell_node_ul.xpath('./li/a')
            # print(len(smell_node_li_list))
            for smell_node_li in smell_node_li_list:
                temp = response.meta
                # 小分类标题
                smell_category_title = smell_node_li.xpath('./text()').extract_first()
                # 小分类链接
                smell_category_link = smell_node_li.xpath('./@href').extract_first()
                temp['smell_category_title'] = smell_category_title
                temp['smell_category_link'] = smell_category_link
                # print(temp)
                # 小链接内容翻页
                for i in range(0, 26):
                    new_page_url = smell_category_link.split("-")[0] + "-24hours-0-0-1-" + str(i+1)
                    print(new_page_url)
                    yield scrapy.Request(url=new_page_url, callback=self.parse_book_list, meta=temp)
                # yield scrapy.Request(url=smell_category_link, callback=self.parse_book_list, meta=temp)

            #     break
            break

    # 获取图书相关信息
    def parse_book_list(self, response):
        # 获取图书信息列表
        book_node_list = response.xpath('/html/body/div[3]/div[3]/div[2]/ul/li')
        # print(len(book_node_list))
        for book_node in book_node_list:
            item = DangdangItem()
            # 书名
            item['book_name'] = book_node.xpath('./div[3]/a/text()').extract_first()
            # 作者
            item['book_author'] = book_node.xpath('./div[5]/a[1]/text()').extract_first()
            # 日期
            item['book_date'] = book_node.xpath('./div[6]/span/text()').extract_first()
            # 出版社
            item['book_press'] = book_node.xpath('./div[6]/a/text()').extract_first()
            # 书价
            item['book_price'] = book_node.xpath('./div[7]/p[1]/span[1]/text()').extract_first()
            # 链接
            item['book_link'] = book_node.xpath('./div[3]/a/@href').extract_first()

            return item
            # break




