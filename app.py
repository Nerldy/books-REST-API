from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class AllBooksResource(Resource):
	"""Handle GET /books"""

	def get(self, book_id):
		return {"book": book_id}


class SingleBookResource(Resource):
	"""Handle GET, PUT, DELETE, POST /book"""

	def get(self, book_id):
		pass

	def post(self, book_id):
		pass


# API Resources
api.add_resource(AllBooksResource, '/books')
api.add_resource(SingleBookResource, '/book/<book_id>')

app.run(port=5000, debug=1)
