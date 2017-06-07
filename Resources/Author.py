import MySQLdb

class Resource:

    def index(self):
        return 'all authors'

    def get(self,id):
        return id