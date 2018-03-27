from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class AllBooksResource(Resource):

	def get(self, book_id):
		return {"book": book_id}


api.add_resource(AllBooksResource, '/books')
