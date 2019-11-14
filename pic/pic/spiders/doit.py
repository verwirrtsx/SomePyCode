# -*- coding: utf-8 -*-
import scrapy
from pic.items import PicItem

class DoitSpider(scrapy.Spider):
    name = 'doit'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/55.html']

    def parse(self, response):
        item =  PicItem()
        imgurls = response.css(".post img::attr(src)").extract()
        item['imgurl'] = imgurls  
        yield item
        pass
