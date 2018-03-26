from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/books')
def get_all_books():
	"""Retrieves all books"""
	return "All Books"



if __name__ == '__main__':
	app.run()
