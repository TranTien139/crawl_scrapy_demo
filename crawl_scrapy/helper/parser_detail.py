__author__ = 'TranTien'

import time
from crawl_scrapy.helper.database import Database


class ParserDetail:
    def __init__(self, response, config):
        result = {}
        try:
            now = time.time()
            result['title'] = response.selector.xpath(config.title).extract_first().encode('utf-8')
            result['description'] = response.selector.xpath(config.description).extract_first().encode('utf-8')
            result['content'] = ''.join(response.selector.xpath(config.content).extract()).encode('utf-8')
            result['thumbnail'] = response.selector.xpath(config.thumbnail).extract_first()
            result['source'] = config.cf_domain
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
