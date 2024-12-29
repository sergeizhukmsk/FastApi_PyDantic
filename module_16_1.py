from fastapi import FastAPI

# Создание экземпляра приложения
app = FastAPI()


# Маршрут - главная страница (/)
# http://127.0.0.1:8000
@app.get("/")
def home():
    return {"message": "Главная страница"}

# Маршрут - страница администратора (/user/admin)
# http://127.0.0.1:8000/user/admin


@app.get("/user/admin")
def admin():
    return {"message": "Вы вошли как администратор"}


# Маршрут - страницы пользователей с параметром в пути (/user/{user_id})
# http://127.0.0.1:8000/user/123
@app.get("/user/{user_id}")
def user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}


# Маршрут - страницы пользователей с данными в запросе (/user?username=...&age=...)
# http://127.0.0.1:8000/user/?username=Sergo&age=62
@app.get("/user/")
def user_info(username: str, age: int):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
