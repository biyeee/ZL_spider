# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request
from zhilian.items import ZhilianItem


class ZlSpiderSpider(scrapy.Spider):
    name = 'zl_spider'
    allowed_domains = ['www.zhaopin.com']
    start_urls = ['https://www.zhaopin.com']
    first_url = 'https://fe-api.zhaopin.com/c/i/sou?start={page}&pageSize=60&cityId=763&workExperience=-1&education' \
                '=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&lastUrlQuery=%7B%22p%22:2,' \
                '%22jl%22:%22763%22,%22kw%22:%22python%22,%22kt%22:%223%22%7D'

    def start_requests(self, page=None):  # 翻页
        for i in range(0, 11):
            page = i*60
            yield Request(self.first_url.format(page=page), callback=self.parse)
        pass

    def parse(self, response):
        item = ZhilianItem()
        result = json.loads(response.text)
        for i in range(0, 60):  # 一个页面有60个数据字典，遍历每个字典
            results = result['data']['results'][i]
            company = results['company']['name']
            eduLevel = results['eduLevel']['name']
            workingExp = results['workingExp']['name']
            city = results['city']['display']
            item['company'] = company
            item['eduLevel'] = eduLevel
            item['salary'] = results.get('salary')
            item['workingExp'] = workingExp
            item['city'] = city
            yield item
