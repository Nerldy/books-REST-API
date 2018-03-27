import unittest
from models import User, Authentication


class ModelsTestCases(unittest.TestCase):
	"""this class tests the models"""

	def test_User_has_get_user_method(self):
		tester = User()
		result = tester.get_username()
		self.assertEqual(result, "John Doe")

	def test_User_has_get_password_method(self):
		tester = User()
		result = tester.get_password()
		self.assertEqual(result, 12345)


if __name__ == '__main__':
	unittest.main()
