# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter


# 使用python的json来保存
# class QsbkPipeline(object):
#     def __init__(self):
#         self.f = open('qsbk.json', 'w', encoding='utf-8')
#
#     # 爬虫开始的时候
#     def open_spider(self, spider):
#         print("爬虫开始.........")
#
#     # 在spider中有爬取数据返回数据的时候
#     def process_item(self, item, spider):
#         # 将爬取的数据保存在json文件中
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.f.write(item_json+'\n')
#         return item
#
#     # 爬虫结束的时候
#     def close_spider(self, spider):
#         print("爬虫结束.....")
#         self.f.close()


# 使用scrapy自带的JsonItemExporter来保存(将全部的数据存放爬取出来后再存放在一个列表中，比较耗用内存）
# class QsbkPipeline(object):
#     def __init__(self):
#         self.f = open('qsbk.json', 'wb')
#         self.exporter = JsonItemExporter(self.f, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     # 爬虫开始的时候
#     def open_spider(self, spider):
#         print("爬虫开始.........")
#
#     # 在spider中有爬取数据返回数据的时候
#     def process_item(self, item, spider):
#         # 将爬取的数据保存在json文件中
#         self.exporter.export_item(item)
#         return item
#
#     # 爬虫结束的时候
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         print("爬虫结束.....")
#         self.f.close()


# 使用scrapy自带的JsonLinesItemExporter来保存(将一行数据爬取后就放在一个字典中）
class QsbkPipeline(object):
    def __init__(self):
        self.f = open('qsbk.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.f, ensure_ascii=False, encoding='utf-8')

    # 爬虫开始的时候
    def open_spider(self, spider):
        print("爬虫开始.........")

    # 在spider中有爬取数据返回数据的时候
    def process_item(self, item, spider):
        # 将爬取的数据保存在json文件中
        self.exporter.export_item(item)
        return item

    # 爬虫结束的时候
    def close_spider(self, spider):
        print("爬虫结束.....")
        self.f.close()
