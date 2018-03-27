# dummy user
users = [
	{
		"id": 1,
		"username": 'nerldy',
		'password': "mic check"
	}
]

username_mapping = {
	"nerldy": {
		"id": 1,
		"username": 'nerldy',
		'password': "mic check"
	}

}

userid_mapping = {
	1: {
		"id": 1,
		"username": 'nerldy',
		'password': "mic check"
	}

}


def authentication(username, password):
	user = username_mapping.get(username, None)
	if user and user.password == password:
		return user


def identity(payload):
	user_id = payload['identity']
	return userid_mapping.get(user_id, None)
