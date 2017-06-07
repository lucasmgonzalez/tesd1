from flask import abort,request
import MySQLdb

class Resource:
    def __init__(self):
        self.db = MySQLdb.connect('192.168.10.10', 'homestead', 'secret', 'tesd1')
        self.cursor = self.db.cursor()

    def index(self):
        sql = "SELECT * FROM authors"
        self.cursor.execute(sql)

        authors = self.cursor.fetchall()

        return authors

    def retrieve(self, id):
        sql = "SELECT * FROM authors WHERE id = '%d'" % id

        self.cursor.execute(sql)

        author = self.cursor.fetchone()

        return author

    def store(self, request):

        # if not request.json or not 'name' in request.json or not 'citation_name' in request.json or not 'cpf' in request.json:
        #     abort(400)

        return len(request)

        # name = request.json['name']
        # citation_name = request.json['citation_name']
        # cpf = request.json['cpf']
        #
        # sql = "INSERT INTO authors (name, citation_name, cpf) VALUES(%s, %s, %s)" % (name, citation_name, cpf)
        #
        # try:
        #     self.cursor.execute(sql)
        #
        #     self.db.commit()
        # except:
        #     self.db.rollback()
        #
        # return True

    def update(self, id, name, citation_name, cpf):
        sql = "UPDATE authors SET name = %s, citation_name = %s, cpf = %s WHERE id = %d" % (name, citation_name, cpf, id)

        try:
            self.cursor.execute(sql)

            self.db.commit()
        except:
            self.db.rollback()

        sql = "SELECT * FROM authors WHERE id = %d" % (id)

        self.cursor.execute(sql)

        author = self.cursor.fetchone()

        return author

    def delete(self, id):

        return True
