import requests

# users = [{"id":1, "username":"SergeiZhuk", "age":62}, {"id":2, "username":"ZhukSergei", "age":62},
# 		 {"id":3, "username":"UrbanUser", "age":24}]

# Данные для обновления
data_1 = {
	'username': 'UrbanUserNew',
	'age': 35
}

data_2 = {
	'username': 'ZhukSergei',
	'age': 62
}
# URL-адрес ресурса, который нужно обновить
url_1 = f"http://127.0.0.1:8000/users/1/{data_1['username']}/{data_1['age']}"
response = requests.put(url_1)

print('status_code = ', response.status_code)

# Проверка статуса ответа 1
if response.status_code == 200:
	print(f"Обновление {response.text} прошло успешно!")
else:
	print(f"1 - Произошла ошибка при обновлении: {response.text}")

url_2 = f"http://127.0.0.1:8000/users/2/{data_2['username']}/{data_2['age']}"
response = requests.put(url_2)

print('status_code = ', response.status_code)

# Проверка статуса ответа 2
if response.status_code == 200:
	print(f"Обновление {response.text} прошло успешно!")
else:
	print(f"2 - Произошла ошибка при обновлении: {response.text}")


