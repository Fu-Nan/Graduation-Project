# -*- coding: utf-8 -*-
import scrapy
from ..items import SysappItem
from scrapy.selector import Selector


class SysappspiderSpider(scrapy.Spider):
    name = 'sysAppSpider'
    allowed_domains = ['mumayi.com']
    start_urls = []
    pageName = 1
    # 生成每页URL地址
    for page in range(pageName):
        start_urls.append(
            "http://www.mumayi.com/android/xitonggongju/list_47_{0}.html".format(page)
        )

    def parse(self, response):
        node_list = response.xpath("/html/body/div[5]/div[2]/div[1]/ul")
        items = []
        for number in range(1, 12):
            for node in node_list:
                item = SysappItem()
                # 应用名称
                item["appName"] = node.xpath("./li[{0}]/a[2]/h3/em/text()".format(number)).extract_first()
                # 应用版本
                item["version"] = node.xpath("./li[{0}]/a[2]/h3/em/span/text()".format(number)).extract_first().strip()
                # 下载次数
                download = node.xpath("./li[{0}]/a[2]/dl/dd[1]/text()".format(number)).extract_first().strip()
                item["download"] = download[5:-1]
                # 应用大小
                size = node.xpath("./li[{0}]/a[2]/dl/dd[2]/text()".format(number)).extract_first().strip()
                item["size"] = size[3:]
                # 推荐指数
                item["vote"] = node.xpath("./li[{0}]/a[2]/dl/dd[3]/span[2]/@class".format(number)).extract_first()[-1:]
                items.append(item)
        return items
