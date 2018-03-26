from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

books = []


class BooksResource(Resource):
	"""This class represents /books"""

	def get(self):
		return books


class BookResource(Resource):
	"""This class represents /books/<book_id>"""

	def get(self, book_id=None):
		""""GET /book/<book_id>"""

		# iterate the books list to search for a book through ID
		for book in books:
			if book['book_id'] == book_id:
				return book

			# return none if book doesn't exists
			return {"book": book_id}

	def post(self, book_id=None):
		"""POST /book/<book_id>"""

		# create a book
		book = {"book_id": book_id, "book_title": "Title of Book"}
		# add it to the book list
		books.append(book)
		return book


api.add_resource(BooksResource, '/books')
api.add_resource(BookResource, '/book/<book_id>')

if __name__ == '__main__':
	app.run(debug=1)
