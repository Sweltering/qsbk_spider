# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        paragraph_divs = response.xpath("//div[@id='content-left']/div")  # 所有段子的div
        for paragraph_div in paragraph_divs:
            author = paragraph_div.xpath(".//h2/text()").get().strip()  # 作者
            content = paragraph_div.xpath(".//div[@class='content']//text()").getall()  # getall返回一个列表，段子文本
            content = "".join(content).strip()  # 段子

            item = QsbkItem(author=author, content=content)  # 使用模型来定义字段数据
            yield item  # 将数据yield到pipline中

        # 下一页的url
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:  # 最后一页,直接返回
            return
        else:
            yield scrapy.Request(self.base_domain+next_url, callback=self.parse)  # 再次请求下一页的数据
