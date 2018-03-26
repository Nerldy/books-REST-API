from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Books(Resource):
	"""This class represents /books"""

	def get(self):
		return {"Hello Books"}


api.add_resource(Books, '/books')

if __name__ == '__main__':
	app.run(debug=1)
