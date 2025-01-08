import logging

# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def create_user() -> User:
	# logging.debug('username - %s, age - %d', username, age)

	# Определяем новый id для пользователя
	next_id = len(users) + 1
	# logging.debug('next_id - %d', next_id)

	# Создаем нового пользователя
	new_user = User(id=next_id, username=username, age=age)
	# logging.debug('new_user - %s', new_user)

# @app.exception_handler(Exception)
# async def validation_exception_handler(request: Request, exc: Exception):
# 	return JSONResponse(status_code=500, content={"message":f"An error occurred: {exc}"})