import MySQLdb

class Resource:
    def __init__(self):
        self.db = MySQLdb.connect('localhost', 'user', '', 'tesd1')
        self.cursor = self.db.cursor()

    def index(self):
        sql = "SELECT * FROM authors"
        self.cursor.execute(sql)

        authors = self.cursor.fetchall()

        return authors

    def get(self,id):
        sql = "SELECT * FROM authors WHERE id = '%d'" % (id)
        self.cursor.execute(sql)

        author = self.cursor.fetchone()

        return author