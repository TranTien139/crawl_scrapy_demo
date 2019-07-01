# _*_ coding: utf8 _*_
# !/usr/bin/env python
__author__ = 'TranTien'


import scrapy
from scrapy.http import Request
from crawl_scrapy.helper.database import Database
from slugify import slugify
import re


class Geographyfieldwork(scrapy.Spider):
    name = 'crawler_province'
    allowed_domain = ['en.wikipedia.org']

    def __init__(self):
        nations = Database()._get_nation()
        self.urls = nations

    def start_requests(self):
        urls = self.urls
        for item in urls:
            url = 'https://en.wikipedia.org/wiki/List_of_cities_in_' + item[1].replace(' ', '_')
            data = {'id': item[0]}
            yield Request(url, self.parse, meta=data, method='get')

        # united state
        # urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']
        # for url in urls:
        #     data = {'id': 191}
        #     yield Request(url, self.parse, meta=data, method='get')

    def parse(self, response):
        try:
            xpath = './/table[contains(@class, "wikitable")]/tbody/tr/td[1]//text() | .//div[@class="div-col columns column-width"]/ul/li/a/text()'

            check_path = response.selector.xpath('.//table[contains(@class, "wikitable")]/tbody/tr/th[2]//text()').extract_first()
            if check_path and ('City' in check_path or 'Name' in check_path or 'Belarusian' in check_path or 'Urban area' in check_path or 'Municipality' in check_path or 'Postal Code' in check_path):
                xpath = './/table[contains(@class, "wikitable")]/tbody/tr/td[2]//text()'

            check_path1 = response.selector.xpath(
                './/table[contains(@class, "wikitable")]/tbody/tr[1]/td[3]//text()').extract_first()
            if check_path1 and ('City' in check_path1 or 'Name' in check_path1):
                xpath = './/table[contains(@class, "wikitable")]/tbody/tr/td[3]//text()'

            check_path2 = response.selector.xpath(
                './/table[contains(@class, "wikitable")]/tbody/tr[1]/th[3]//text()').extract_first()
            if check_path2 and ('City' in check_path2 or 'Name' in check_path2 or 'Province' in check_path2) and ('Official Name' not in check_path2):
                xpath = './/table[contains(@class, "wikitable")]/tbody/tr/td[3]//text()'

            # united state
            # xpath = './/table[contains(@class, "wikitable")][2]/tbody/tr/td[2]//text()'

            datas = response.selector.xpath(xpath).extract()
            for item in datas:
                result1 = re.findall(r'\((.*?)\)', item)
                for rex1 in result1:
                    item = item.replace('(' + rex1 + ')', '')

                result2 = re.findall(r'\[(.*?)\]', item)
                for rex2 in result2:
                    item = item.replace('[' + rex2 + ']', '')
                item = item.replace('(', '').replace(')', '').replace('*','').replace('/','').replace(':', ' ').replace('.', ' ').replace(',',' ')
                array = re.findall(r'[0-9]+', item)
                for num in array:
                    item = item.replace(num, '')
                item = item.strip()
                if item:
                    new_Data = {'name': item, 'parent_id': response.meta['id']}
                    Database()._insert_province(new_Data)
                    print(item, response.meta['id'])
        except Exception as e:
            print('co loi xay ra khi lay link bai viet', e)
