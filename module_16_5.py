from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


# Создаем экземпляр приложения FastAPI
app = FastAPI()


# Настраиваем Jinja2 для загрузки шаблонов из папки templates
templates = Jinja2Templates(directory="templates")

# Список пользователей
users = []


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
