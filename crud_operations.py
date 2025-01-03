from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {"id": 1, "description": "Изучить CRUD в FastAPI"},
    {"id": 2, "description": "Написать примеры кода"}
]


# Получить список всех задач
@app.get("/tasks")
async def get_tasks():
    return tasks


# Получить задачу по ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

raise HTTPException(status_code=404, detail="Задача не найдена")


# Создать новую задачу
@app.post("/tasks")
async def create_task(description: str):
    if not tasks:  # if len(tasks) == 0:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1

    new_task = {"id": new_id, "description": description}
    tasks.append(new_task)
    return new_task


# Обновить задачу по ID
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, description: str):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
        return task
    raise HTTPException(status_code=404, detail="Задача не найдена")


# Удалить задачу по ID
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
        return {"detail": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")


# PATCH — Частичное обновление данных
@app.patch("/tasks/{task_id}")
async def patch_task(task_id: int, description: str = None):
    for task in tasks:
        if task["id"] == task_id:
            if description:
                task["description"] = description
            return task

    raise HTTPException(status_code=404, detail="Задача не найдена")
