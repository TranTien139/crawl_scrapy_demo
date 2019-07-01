import MySQLdb
from scrapy.conf import settings
from slugify import slugify

__author__ = 'TranTien'


class Database:
    def __init__(self):
        self.conn = MySQLdb.connect(host=settings['MYSQL_HOST'], port=int(settings['MYSQL_PORT']),
                                    user=settings['MYSQL_USER'], passwd=settings['MYSQL_PASSWORD'],
                                    db=settings['MYSQL_DB'], charset="utf8", use_unicode=True)
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

    def _insert_nation(self, item):
        try:
            check = self.cursor.execute("""SELECT * FROM locations WHERE name=%s""", [item['name']])
            if not check:
                slug = slugify(item["name"])
                self.cursor.execute("""INSERT INTO locations (name, code, type) VALUES (%s, %s, %s)""", (item["name"], slug, 'nation'))
                self.conn.commit()
                print('Luu du lieu thanh cong')
            return item
        except Exception as e:
            print('Co loi xay ra khi luu post', e)
            return item


    def _get_nation(self):
        try:
            self.cursor.execute("""SELECT * FROM locations  WHERE parent_id IS NULL limit 0, 210""")
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('Co loi xay ra khi luu post', e)
            return None

    def _insert_province(self, item):
        try:
            check = self.cursor.execute("""SELECT * FROM locations WHERE name=%s AND parent_id=%s""", [item['name'], int(item["parent_id"])])
            if not check:
                slug = slugify(item["name"])
                self.cursor.execute("""INSERT INTO locations (name, code, type, parent_id) VALUES (%s, %s, %s, %s)""", (item["name"], slug, 'province', int(item["parent_id"])))
                self.conn.commit()
                print('Luu du city thanh cong')
            return item
        except Exception as e:
            print('Co loi xay ra khi luu city', e)
            return item