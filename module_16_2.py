from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()


# http://127.0.0.1:8000/users/55
@app.get("/users/{user_id}")
async def get_user(user_id: Annotated[int, Path(ge=0, le=100, title="Enter User ID",
        description="ID должен быть положительным целым числом")]):
    return {"user_id": user_id}


# http://127.0.0.1:8000/users/Sergo/62
@app.get("/users/{username}/{age}")
async def get_user_by_username(
        username: Annotated[str, Path(min_length=5, max_length=20, title="Enter username", regex="^[a-zA-Z0-9_-]+$")],
        age: Annotated[int, Path(ge=18, le=120, title="Enter Age", description="Возраст должен быть положительным")]):
    return {"username": username, "age": age}

# Чтобы запустить приложение, используйте команду:
# uvicorn module_16_3:app --reload
