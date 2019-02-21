__author__ = 'TranTien'

import configparser
from scrapy.conf import settings


class LoadConfig:
    def __init__(self, cf_domain=''):
        parse_cate = configparser.ConfigParser()
        parse_cate.read(settings.get('PARSER_CONFIG_FILE'), encoding="utf8")
        self.parse_cate = parse_cate
        self.cf_domain = cf_domain
        self.title = self.parse_cate.get(self.cf_domain, 'title_select')
        self.description = self.parse_cate.get(self.cf_domain, 'description_select')
        self.content = self.parse_cate.get(self.cf_domain, 'content_select')
        self.thumbnail = self.parse_cate.get(self.cf_domain, 'thumbnail_select')
        self.category_link = self.parse_cate.get(self.cf_domain, 'category_link_select')
