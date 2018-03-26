from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
	"""
	:return: Home page
	"""
	return "Hello World"


@app.route('/books')
def get_all_books():
	"""
	:return: All books
	"""
	return 'get all books'


if __name__ == '__main__':
	app.run(debug=1)
