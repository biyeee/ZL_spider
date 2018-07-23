# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    eduLevel = scrapy.Field()  # 学历
    company = scrapy.Field()  # 公司名称
    salary = scrapy.Field()  # 薪资
    city = scrapy.Field()  # 城市
    workingExp = scrapy.Field()  # 工作经验

