from flask import Flask, jsonify
from flask_cors import CORS 

# instantiate the application
app = Flask(__name__)
app.config.from_object(__name__)

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })

if __name__ == '__main__':
    app.run()

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True,
    },
        {
        'title': 'Harry Potter and the Philosoph\'s Stone',
        'author': 'J. K. Rowling',
        'read': True,
    },
    {
        'title': 'Lord of the Rings: The Hobbit',
        'author': 'J. R. R. Tolkien',
        'read': True,
    },
]

