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


class Authentication(User):
	"""class to authenticate the user"""

	def __init__(self, username, password):
		super().__init__(username, password)

	def get_authentication(self, username, password):
		pass
