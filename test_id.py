users = [{"id":5, "username":"UrbanUser - 3", "age":22},
		 {"id":2, "username":"ZhukSergei", "age":62},
		 {"id":3, "username":"UrbanUser - 1", "age":20},
		 {"id":4, "username":"UrbanUser - 2", "age":21},
		 {"id":1, "username":"SergeiZhuk", "age":62},
		 {"id":6, "username":"UrbanUser - 4", "age":23},
		 {"id":7, "username":"UrbanUser - 5", "age":24},
		 {"id":8, "username":"UrbanUser - 6", "age":25}]

# user = next((user for i, user in enumerate(users) if i == 2), None)
# user = next((user for user in users if user["id"] == '2'), None)


# for user in users:
# 	#print('user = ', user, '  user_id = ', user['id'])
#
# 	#print(user['id'], user['username'], user['age'], user['id'] == 3)
# 	if user['id'] == 2:
# 		#print('Вошел по условию!')
# 		user_one = users[user['id']]
# 		#input('Ждем')
# 		#print('user_one', user_one)
# 		break
	# else:
	# 	user_one = [{"id": 5, "username": "UrbanUser - 3", "age": 22}]

user_id = 3
user_one = next((user for user in users if user['id'] == user_id), None)

print('End - user_one', user_one)
