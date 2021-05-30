# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SysappItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 应用名称
    appName = scrapy.Field()
    # 应用版本
    version = scrapy.Field()
    # 下载次数
    download = scrapy.Field()
    # 应用大小
    size = scrapy.Field()
    # 推荐指数
    vote = scrapy.Field()
