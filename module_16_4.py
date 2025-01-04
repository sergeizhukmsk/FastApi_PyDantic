from typing import Annotated, List
from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Список пользователей
users = []


class User(BaseModel):
	id: int  # номер пользователя (int)
	username: str  # имя пользователя (str)
	age: int  # возраст пользователя (int)


# Возвращает всех пользователей
@app.get("/users", response_model=List[User])
def get_users() -> List[User]:
	return users


# Добавление нового пользователя
@app.post("/users/{username}/{age}", response_model=User)
def create_user(
		username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username", regex="^[a-zA-Z0-9_-]+$")],
		age: Annotated[int, Path(ge=18, le=120, title="Enter Age", description="Возраст должен быть положительным")]
) -> User:

	# Определяем новый id для пользователя
	next_id = len(users) + 1

	# Создаем нового пользователя
	new_user = User(id=next_id, username=username, age=age)

	if isinstance(new_user, User):
		users.append(new_user)
	else:
		print('Error: new_user is not an instance of User')

	return new_user


# Обновление существующего пользователя
@app.put("/users/{user_id}/{username}/{age}", response_model=User)
def update_user(
		user_id: Annotated[
			int, Path(ge=1, title="Enter User ID", description="ID должен быть положительным целым числом")],
		username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username", regex="^[a-zA-Z0-9_-]+$")],
		age: Annotated[int, Path(ge=18, le=120, title="Enter Age", description="Возраст должен быть положительным")]
) -> User:

	user = next((user for user in users if user.id == user_id), None)

	if user is None:
		raise HTTPException(status_code=404, detail="User was not found")
	else:

		if isinstance(user, User):
			user.username = username
			user.age = age
		else:
			print('Error: user is not an instance of User')

	return user


# Удаление пользователя
@app.delete("/users/{user_id}", response_model=User)
def delete_user(
		user_id: Annotated[
			int, Path(ge=1, title="Enter User ID", description="ID должен быть положительным целым числом")]
) -> User:
	user = next((user for user in users if user.id == user_id), None)

	if user is None:
		raise HTTPException(status_code=404, detail="User was not found")
	else:
		if isinstance(user, User):
			users.remove(user)  # Удаляем пользователя из списка
		else:
			print('Error: user is not an instance of User')

	return user

# Чтобы запустить приложение, используйте команду:
# uvicorn module_16_4:app --reload
