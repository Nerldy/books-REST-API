from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Books list
books = []


class AllBooksResource(Resource):
	"""Handle GET /books"""

	def get(self):
		if books:
			return {"books": books}

		return {"books": "No books found"}


class SingleBookResource(Resource):
	"""Handle GET, PUT, DELETE, POST /book"""

	def get(self, book_id):

		for book in books:
			if book["book_id"] == book_id:
				return {"book_id": book[book_id]}, 200
			return {"message": f"Book with id {book_id} not found"}, 404

	def post(self, book_id):

		for book in books:
			if book["book_id"] == book_id:
				return {"message": f"Book with id {book_id} already exists."}, 400

		book = {"book_id": book_id}
		books.append(book)
		return book, 201

	def delete(self, book_id):
		global books
		books = list(filter(lambda x: x["book_id"] != book_id, books))
		return {"message": "book deleted"}


# API Resources
api.add_resource(AllBooksResource, '/books')
api.add_resource(SingleBookResource, '/book/<book_id>')

app.run(port=5000, debug=1)
