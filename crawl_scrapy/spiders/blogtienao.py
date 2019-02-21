# _*_ coding: utf8 _*_
# !/usr/bin/env python
__author__ = 'TranTien'


import scrapy
from scrapy.http import Request
from crawl_scrapy.helper.init_config import LoadConfig
from crawl_scrapy.helper.parser_detail import ParserDetail


class BlogTienAo(scrapy.Spider):
    name = 'blogtienao'
    allowed_domain = ['blogtienao.com']

    def __init__(self):
        self.config = LoadConfig('blogtienao.com')

    def start_requests(self):
        urls = [
            'https://blogtienao.com'
        ]
        for url in urls:
            yield Request(url, self.parse)

    def parse(self, response):
        try:
            post_urls = response.selector.xpath(self.config.category_link).extract()
            for url in post_urls:
                meta = {'url': url}
                yield Request(url, callback=self.parse_full_post, meta=meta, method='get')
        except Exception as e:
            print('co loi xay ra khi lay link bai viet', e)

    def parse_full_post(self, response):
        ParserDetail(response, self.config)

