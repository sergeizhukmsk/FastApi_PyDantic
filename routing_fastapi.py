from fastapi import FastAPI

app = FastAPI()


# Пример простого маршрута
@app.get("/")
async def read_root() -> dict:
    return {"message": "Hello, Urban’s student!"}


# Пример динамического параметра в маршруте
@app.get("/users/{user_id}")
async def get_user(user_id: int) -> dict:
    return {"user_id": user_id, "name": f"User {user_id}"}


# Пример использования Query Parameters
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10) -> dict:
    items = [{"item_id": i} for i in range(skip, skip + limit)]
    return {"items": items}


# Пример совмещения динамических параметров и параметров запроса
@app.get("/products/{product_id}")
async def read_product(product_id: int, details: bool = False) -> dict:
    product_info = {"product_id": product_id, "name": f"Product {product_id}"}
    if details:
        product_info["details"] = "Detailed product information"
        return product_info


# Пример с пересечением маршрутов - Рассмотрим два маршрута:
@app.get("/items/new")
async def read_new_items() -> dict:
    return {"message": "This is a list of new items"}


@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id, "name": f"Item {item_id}"}


# Пример маршрута с несколькими параметрами
@app.get("/categories/{category_id}/items/{item_id}")
async def read_category_item(category_id: int, item_id: int) -> dict:
    return {"category_id": category_id, "item_id": item_id}


# Пример путей с фиксированными и динамическими частями
@app.get("/users/me")
async def read_current_user() -> dict:
    return {"user": "This is the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: int) -> dict:
    return {"user_id": user_id, "name": f"User {user_id}"}
