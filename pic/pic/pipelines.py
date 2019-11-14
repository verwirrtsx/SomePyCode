# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class PicPipeline(object):
    def get_media_requests(self, item, info):
        for file_url in item['imgurl']:
            yield scrapy.Request(file_url)
