class User:
	"""creates user"""

	def __init__(self, _id=None, username='John Doe', password=12345):
		self.id = _id
		self.username = username
		self.password = password

	def get_username(self):
		"""returns username"""
		return self.username

	def get_password(self):
		"""returns password"""
		return self.password


class Book:
	"""book attributes"""

	def __init__(self, book_id=0, book_title='', isbn_number=0):
		self.book_id = book_id
		self.book_title = book_title
		self.book_isbn = isbn_number
		self.book_author = []

	def set_book_author(self, first_name, last_name):
		"""creates a new author"""
		self.first_name = first_name
		self.last_name = last_name
		full_name = f"{self.first_name} {self.last_name} "
		self.book_author.append(full_name)

	def get_author(self):
		"""returns book author list"""
		return self.book_author
