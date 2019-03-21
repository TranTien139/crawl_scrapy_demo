# _*_ coding: utf8 _*_
# !/usr/bin/env python
__author__ = 'TranTien'


import scrapy
from scrapy.http import Request
from crawl_scrapy.helper.database import Database


class Geographyfieldwork(scrapy.Spider):
    name = 'geographyfieldwork'
    allowed_domain = ['geographyfieldwork.com']

    def __init__(self):
        pass

    def start_requests(self):
        urls = [
            'https://geographyfieldwork.com/WorldCapitalCities.htm'
        ]
        for url in urls:
            yield Request(url, self.parse)

    def parse(self, response):
        try:
            datas = response.xpath('//*/table[@id="anyid"]/tr')
            for item in datas[1:]:
                result = dict()
                result['nation'] = item.xpath('td[@height=17][1]/text()').extract_first()
                result['capital'] = item.xpath('td[@height=17][2]/text()').extract_first()
                if result['nation'] and result['capital']:
                    Database()._insert_nation(result)
                    print(result)
        except Exception as e:
            print('co loi xay ra khi lay link bai viet', e)
