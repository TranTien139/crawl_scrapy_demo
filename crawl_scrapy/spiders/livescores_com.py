import scrapy
from scrapy_splash import SplashRequest
from crawl_scrapy.helper.init_config import LoadConfig

class Livescores(scrapy.Spider):
    name = 'livescores'
    allowed_domain = ['livescores.com']

    def __init__(self):
        self.config = LoadConfig('livescores.com')

    def start_requests(self):
        url = 'https://livescores.com'

        splash_args = {
            'html': 1,
            'png': 1,
            'width': 600,
            'render_all': 1,
        }

        yield SplashRequest(url, self.parse_result, endpoint='render.json', args=splash_args)

    def parse_result(self, response):
        try:
            post_html = response.selector.xpath(self.config.title).extract_first()
            print(post_html)
        except Exception as e:
            print('error :' , e)