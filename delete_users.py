import requests

# users = [{"id":1, "username":"SergeiZhuk", "age":62}, {"id":2, "username":"ZhukSergei", "age":62},
# 		 {"id":3, "username":"UrbanUser", "age":24}]

# ID пользователя, которого нужно удалить
user_id_to_delete = 3

# URL-адрес ресурса, который нужно удалить
url = f"http://127.0.0.1:8000/users/{user_id_to_delete}"
#url = f"http://127.0.0.1:8000/users/3"

# Выполнение DELETE-запроса
response = requests.delete(url)

print('status_code = ', response.status_code)

# Проверка статуса ответа
if response.status_code == 200:
	print(f"Пользователь: {response.text} удалён успешно!")
else:
	print(f"Произошла ошибка при удалении: {response.text}")
