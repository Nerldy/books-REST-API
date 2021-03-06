from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import identity, authentication

app = Flask(__name__)
app.secret_key = 'test'
api = Api(app)

jwt = JWT(app, authentication, identity)

# Books list
books = []


class AllBooksResource(Resource):
	"""Handle GET /books"""

	@jwt_required()
	def get(self):
		if books:
			return {"books": books}

		return {"books": "No books found"}


class SingleBookResource(Resource):
	"""Handle GET, PUT, DELETE, POST /book"""

	def get(self, book_id):
		"""handles GET /boo"""
		book = next(filter(lambda x: x["book_id"] == book_id, books), None)
		return {'book': book}, 200 if book else 404

	def post(self, book_id):

		for book in books:
			if book["book_id"] == book_id:
				return {"message": f"Book with id {book_id} already exists."}, 400

		data = request.get_json()
		book = {"book_id": book_id, "title": data['title']}
		books.append(book)
		return book, 201

	def delete(self, book_id):
		global books
		books = list(filter(lambda x: x["book_id"] != book_id, books))
		return {"message": "book deleted"}

	def put(self, book_id):
		data = request.get_json()
		book = next(filter(lambda x: x["book_id"] == book_id, books), None)

		if book is None:
			book = {"book_id": book_id, "title": data['title']}
			books.append(book)
		else:
			book.update(data)

		return book


# API Resources
api.add_resource(AllBooksResource, '/books')
api.add_resource(SingleBookResource, '/book/<book_id>')

app.run(port=5000, debug=1)
