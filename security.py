from models import User

# dummy user
users = [
	User(1, 'nerldy', 'mic check')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authentication(username, password):
	user = username_mapping.get(username, None)
	if user and user.password == password:
		return user


def identity(payload):
	user_id = payload['identity']
	return userid_mapping.get(user_id, None)
