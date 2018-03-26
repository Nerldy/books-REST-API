from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Books(Resource):
	def get(self):
		pass
