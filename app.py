from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/books', methods=['POST'])
def post_book():
	return "Books"


@app.route('/books')
def get_all_books():
	"""Retrieves all books"""
	return "All Books"


if __name__ == '__main__':
	app.run()
