from flask import Flask, jsonify
from Resources import Author

app = Flask(__name__)

author_resource = Author.Resource()

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/authors', methods=['GET'])
def get_authors():
    return jsonify(author_resource.index())

@app.route('/author/<int:id>', methods=['GET'])
def get_author(id):
    return jsonify(author_resource.get(id))

if __name__ == '__main__':
    app.run(debug=True)


