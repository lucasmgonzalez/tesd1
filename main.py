from flask import Flask, jsonify, request
import json
from Resources import Author

app = Flask(__name__)

author_resource = Author.Resource()


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/authors', methods=['GET'])
def get_authors():
    return author_resource.index()


@app.route('/author', methods=['POST'])
def create_author():
    return author_resource.store(request)


@app.route('/author/<int:id>', methods=['GET'])
def retrieve_author(id):
    return author_resource.retrieve(id)


if __name__ == '__main__':
    app.run(debug=True)


