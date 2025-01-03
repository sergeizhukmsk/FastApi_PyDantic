from typing import Annotated, Dict
from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

# Словарь пользователей
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


# Возвращает всех пользователей
@app.get("/users")
def get_users():
	return users


# Добавление нового пользователя
@app.post("/users/{username}/{age}")
def create_user(
	username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username", regex="^[a-zA-Z0-9_-]+$")],
	age: Annotated[int, Path(ge=18, le=120, title="Enter Age", description="Возраст должен быть положительным")]
	):

	# Находим максимальный ключ
	max_id = max(map(int, users.keys()), default=0)
	new_id = str(max_id + 1)

	# Добавляем нового пользователя
	users[new_id] = f"Имя: {username}, возраст: {age}"
	return f"Пользователь: {username}, возраст: {age}, номер записи {new_id} зарегистрирован"


# Обновление существующего пользователя
@app.put("/users/{user_id}/{username}/{age}")
def update_user(user_id: Annotated[
	int, Path(ge=0, le=100, title="Enter User ID", description="ID должен быть положительным целым числом")],
				username: Annotated[
					str, Path(min_length=5, max_length=20, title="Enter username", regex="^[a-zA-Z0-9_-]+$")],
				age: Annotated[
					int, Path(ge=18, le=120, title="Enter Age", description="Возраст должен быть положительным")]
				):

	if str(user_id) not in users:
		raise HTTPException(status_code=404, detail=f'Пользователь {user_id} не найден в словаре')

	users[str(user_id)] = f'Имя: {username}, возраст: {age}'  # Обновляем данные пользователя

	return {"message": f'Номер записи {user_id}: Пользователь {username}, возраст: {age} - обновлен'}


# Удаление пользователя
@app.delete("/users/{user_id}")
def delete_user(
		user_id: Annotated[
			int, Path(ge=0, le=100, title="Enter User ID", description="ID должен быть положительным целым числом")]):

	if str(user_id) not in users:
		raise HTTPException(status_code=404, detail=f'Пользователь {user_id} не найден в словаре')

	del users[str(user_id)]  # Удаляем пользователя из словаря

	return {"message": f'Запись с номером {user_id} успешно удалена'}


# Чтобы запустить приложение, используйте команду:
# uvicorn module_16_3:app --reload
