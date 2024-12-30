# Пример простой аннотации с Path
from typing import Annotated
from fastapi import FastAPI, Path
from enum import Enum

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="ID of the item")):
    return {"item_id": item_id}


# Пример аннотации с использованием Annotated
@app.get("/users/{user_id}")
async def get_user(user_id: Annotated[int, Path(gt=0, title="User ID", description="Идентификатор должен быть положительным целым числом")]):
    return {"user_id": user_id}


# Валидация чисел (int, float)
@app.get("/products/{product_id}")
async def get_product(
        product_id: Annotated[int, Path(gt=0, le=1000, description="Product ID from 1 to 1000")],
        rating: Annotated[float, Path(gt=0, le=5, description="Product rating from 0 to 5")]
):
    return {"product_id": product_id, "rating": rating}

# Можно использовать gt (greater than), ge (greater than or equal), lt (less than), и le (less than or equal)
# gt (greater than) - больше, чем
# ge (greater than or equal) - больше или равно
# lt (less than) - меньше, чем
# le (less than or equal) – меньше или равно

# Валидация строк (str)
@app.get("/users/{username}")
async def get_user_by_username(
        username: Annotated[str, Path(min_length=3, max_length=20, regex="^[a-zA-Z0-9_-]+$")]
):
    return {"username":username}


# Валидация значений с ограниченным выбором (Enum)
class Category(str, Enum):
    electronics = "electronics"


clothing = "clothing"
books = "books"


@app.get("/categories/{category}")
async def get_category(
        category: Annotated[Category, Path(description="Category of items")]
):
    return {"category": category}


# Пример комбинированной валидации
@app.get("/orders/{order_id}")
async def get_order(
        order_id: Annotated[int, Path(gt=0, description="Positive integer for the order ID")],
        customer_name: Annotated[str, Path(min_length=3, max_length=50, regex="^[A-Za-z\\s]+$",
                                           description="Имя должно содержать только буквы и пробелы")],
):
    return {"order_id": order_id, "customer_name": customer_name}
