class User:
	"""creates user"""

	def __init__(self, username='John Doe', password=12345):
		self.username = username
		self.password = password

	def get_username(self):
		return self.username

	def get_password(self):
		return self.password


class Authentication(User):
	"""class to authenticate the user"""

	def __init__(self, username, password):
		super().__init__(username, password)

	def get_authentication(self, username, password):
		pass
