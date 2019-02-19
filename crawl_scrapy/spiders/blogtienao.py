# _*_ coding: utf8 _*_
# !/usr/bin/env python

__author__ = 'TranTien'

import scrapy
from scrapy.http import Request
import time
from crawl_scrapy.database import Database
import configparser
from scrapy.conf import settings


class BlogTienAo(scrapy.Spider):

    name = 'blogtienao'
    allowed_domain = ['blogtienao.com']

    def __init__(self, service_id=None, *args, **kwargs):

        parse_cate = configparser.ConfigParser()
        parse_cate.read(settings.get('PARSER_CONFIG_FILE'), encoding="utf8")
        self.parse_cate = parse_cate
        self.service_id = 0
        self.cookies = {}
        self.cf_domain = 'blogtienao.com'
        self.post_title = self.parse_cate.get(self.cf_domain, 'post_title_select')
        self.post_description = self.parse_cate.get(self.cf_domain, 'post_description_select')
        self.post_content = self.parse_cate.get(self.cf_domain, 'post_content_select')
        self.post_created_at = self.parse_cate.get(self.cf_domain, 'post_created_at_select')
        self.post_time = self.parse_cate.get(self.cf_domain, 'post_time_select')
        self.post_image = self.parse_cate.get(self.cf_domain, 'post_image_select')
        self.post_category_link = self.parse_cate.get(self.cf_domain, 'post_category_link_select')

    def start_requests(self):
        urls = [
            'https://blogtienao.com/'
        ]
        for url in urls:
            yield Request(url, self.parse)

    def parse(self, response):
        try:
            post_urls = response.selector.xpath(self.post_category_link).extract()
            for url in post_urls:
                meta = {'url': url}
                yield Request(url, callback=self.parse_full_post, meta=meta, method='get')
        except Exception as e:
            print('co loi xay ra khi lay link bai viet', e)

    def parse_full_post(self, response):
        result = {}
        try:
            now = time.time()
            result['title'] = response.selector.xpath(self.post_title).extract_first().encode('utf-8')
            result['description'] = response.selector.xpath(self.post_description).extract_first().encode('utf-8')
            result['content'] = ''.join(response.selector.xpath(self.post_content).extract()).encode('utf-8')
            result['source'] = self.cf_domain
            result['created_at'] = now
            result['updated_at'] = now
            result['origin_url'] = response.meta['url'].encode('utf-8')
            result['published_at'] = None
            print('----------------------------------------------------------------')
            print(result)
            Database()._insert_post(result)
            print('----------------------------------------------------------------')
        except Exception as e:
            print('co loi xay ra khi lay chi tiet bai viet', e)
