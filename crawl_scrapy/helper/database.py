import MySQLdb
from scrapy.conf import settings

__author__ = 'TranTien'


class Database:
    def __init__(self, *args, **kwargs):
        self.conn = MySQLdb.connect(settings['MYSQL_HOST'], settings['MYSQL_USER'], settings['MYSQL_PASSWORD'],
                                    settings['MYSQL_DB'], charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def _insert_post(self, item):
        try:
            check = self.cursor.execute("""SELECT * FROM article WHERE origin_url=%s""", [item['origin_url']])
            if not check:
                self.cursor.execute("""INSERT INTO article
                (title, description, content, origin_url, source, created_at, updated_at, published_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                                    (item["title"], item["description"], item["content"], item["origin_url"],
                                     item['source'], item["created_at"], item["updated_at"], item["published_at"]))
                self.conn.commit()
                print('Luu du lieu thanh cong')
            return item
        except Exception as e:
            print('Co loi xay ra khi luu post', e)
            return item