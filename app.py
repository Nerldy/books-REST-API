from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = []


class BooksResource(Resource):
	"""This class represents /books"""

	def get(self):
		return {"books": books}


class BookResource(Resource):
	"""This class represents /books/<book_id>"""

	def get(self, book_id=None):
		""""GET /book/<book_id>"""

		# iterate the books list to search for a book through ID
		book = next(filter(lambda b: b['book_id'] == book_id, books), None)

		# return none if book doesn't exists
		return {"book": book}, 200 if book else 404


def post(self, book_id=None):
	"""POST /book/<book_id>"""
	data = request.get_json()
	# create a book
	book = {"book_id": book_id, "book_title": data['book_title']}
	# add it to the book list
	books.append(book)
	return book, 201


api.add_resource(BooksResource, '/books')
api.add_resource(BookResource, '/book/<book_id>')

if __name__ == '__main__':
	app.run(debug=1)
