from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


# Создаем экземпляр приложения FastAPI
app = FastAPI(debug=True)


# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")

# Список пользователей
#users = []


users = [{"id":5, "username":"UrbanUser - 3", "age":22},
		 {"id":2, "username":"ZhukSergei", "age":62},
		 {"id":3, "username":"UrbanUser - 1", "age":20},
		 {"id":4, "username":"UrbanUser - 2", "age":21},
		 {"id":1, "username":"SergeiZhuk", "age":62},
		 {"id":6, "username":"UrbanUser - 4", "age":23},
		 {"id":7, "username":"UrbanUser - 5", "age":24},
		 {"id":8, "username":"UrbanUser - 6", "age":25}]


class User(BaseModel):
	id: int  # номер пользователя (int)
	username: str  # имя пользователя (str)
	age: int  # возраст пользователя (int)


# Главная страница с пользователями -  -> HTMLResponse
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
	return templates.TemplateResponse("users.html", {"request": request, "users_list": users})


# Главная страница с пользователями
@app.get("/users/", response_class=HTMLResponse)
async def read_users(request: Request):
	return templates.TemplateResponse("users.html", {"request": request, "users_list": users})


# Страница конкретного пользователя
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: int):
	user_one = next((user for user in users if user['id'] == user_id), None)
	if type(user_one) is not list:
		user_one = [user_one]
	return templates.TemplateResponse("users.html", {"request": request, "user_list": user_one})


# Чтобы запустить приложение, используйте команду:
# uvicorn module_16_5:app --reload
# uvicorn module_16_5:app --host 127.0.0.1 --port 5000 --reload
# uvicorn module_16_5:app --host 127.0.0.1 --port 8000 --reload
