__author__ = 'TranTien'

# from crawl_scrapy.helper.database import Database
from crawl_scrapy.helper.clean_time import CleanTime

class ParserDetail:
    def __init__(self, response, config):
        result = {}
        try:
            result['title'] = response.selector.xpath(config.title).extract_first()
            result['description'] = response.selector.xpath(config.description).extract_first()
            result['content'] = ''.join(response.selector.xpath(config.content).extract())
            result['thumbnail'] = response.selector.xpath(config.thumbnail).extract_first()
            result['source'] = response.meta['url']
            result['date'] = response.selector.xpath(config.date).extract_first()
            result['date'] = CleanTime().clean_date(result['date'])
            result['category'] = response.selector.xpath(config.category).extract()
            result['keyword'] = response.selector.xpath(config.keyword).extract()
            print('----------------------------------------------------------------')
            print(result)
            print('----------------------------------------------------------------')
        except Exception as e:
            print('co loi xay ra khi lay chi tiet bai viet', e)
