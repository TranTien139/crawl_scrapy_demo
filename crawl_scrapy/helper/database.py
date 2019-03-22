import MySQLdb
from scrapy.conf import settings

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
            check = self.cursor.execute("""SELECT * FROM nations WHERE name=%s""", [item['name']])
            if not check:
                self.cursor.execute("""INSERT INTO nations (name, capital) VALUES (%s, %s)""", (item["name"], item["capital"]))
                self.conn.commit()
                print('Luu du lieu thanh cong')
            return item
        except Exception as e:
            print('Co loi xay ra khi luu post', e)
            return item


    def _get_nation(self):
        try:
            self.cursor.execute("""SELECT * FROM nations limit 0, 210""")
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print('Co loi xay ra khi luu post', e)
            return None

    def _insert_province(self, item):
        try:
            check = self.cursor.execute("""SELECT * FROM provinces WHERE name=%s AND nation_id=%s""", [item['name'], int(item["nation_id"])])
            if not check:
                self.cursor.execute("""INSERT INTO provinces (name, nation_id) VALUES (%s, %s)""", (item["name"], int(item["nation_id"])))
                self.conn.commit()
                print('Luu du city thanh cong')
            return item
        except Exception as e:
            print('Co loi xay ra khi luu city', e)
            return item