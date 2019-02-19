# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
from pathlib import Path

BOT_NAME = 'crawl_scrapy'
SPIDER_MODULES = ['crawl_scrapy.spiders']
NEWSPIDER_MODULE = 'crawl_scrapy.spiders'

ROBOTSTXT_OBEY = True

PARSER_CONFIG_FILE = './parser_config.cfg'

env_path = Path('.') / '.env'
print(env_path)
if not env_path.is_file():
    print('Load congig mysql from file .env.example')
    env_path = Path('.') / '.env.example'

load_dotenv(dotenv_path=env_path)

DOWNLOAD_DELAY = 5
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')

print(MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD,MYSQL_DB )
