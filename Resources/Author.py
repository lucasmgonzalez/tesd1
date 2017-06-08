from flask import abort,request, jsonify
import MySQLdb
import json

class Resource:
    def __init__(self):
        self.db = MySQLdb.connect('192.168.10.10', 'homestead', 'secret', 'tesd1')
        self.cursor = self.db.cursor()

    def index(self):
        sql = "SELECT * FROM authors"
        self.cursor.execute(sql)

        authors = self.cursor.fetchall()

        return jsonify(authors)

    def retrieve(self, id):
        sql = "SELECT * FROM authors WHERE id = '%d'" % id

        self.cursor.execute(sql)

        # Check if model was found

        author = self.cursor.fetchone()

        return jsonify(author)

    def store(self, request):

        if not request.json or not 'name' in request.json or not 'citation_name' in request.json or not 'cpf' in request.json:
            abort(400)

        name = request.json['name']
        citation_name = request.json['citation_name']
        cpf = request.json['cpf']

        sql = "INSERT INTO authors (name, citation_name, cpf) VALUES('%s', '%s', '%s')" % (name, citation_name, cpf)

        try:
            self.cursor.execute(sql)

            self.db.commit()
        except:
            self.db.rollback()

            abort(500)

        return jsonify({'message': 'created'})

    def update(self, id, request):
        select_sql = "SELECT * FROM authors WHERE id = %d" % id

        self.cursor.execute(select_sql)

        # Check if model was found

        author = self.cursor.fetchone()

        name = request.json.get('name', author[1])
        citation_name = request.json.get('citation_name', author[2])
        cpf = request.json.get('cpf', author[3])

        sql = "UPDATE authors SET name = '%s', citation_name = '%s', cpf = '%s' WHERE id = %d" % \
              (name, citation_name, cpf, id)

        try:
            self.cursor.execute(sql)

            self.db.commit()
        except:
            self.db.rollback()

            abort(500)

        return jsonify({'message': 'updated'})

    def delete(self, id):

        sql = "DELETE FROM authors WHERE id = %d" % id

        try:
            self.cursor.execute(sql)

            self.db.commit()
        except:
            self.db.rollback()

            abort(500)

        return jsonify({'message': 'deleted'})

