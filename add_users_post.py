import requests

url_1 = "http://127.0.0.1:8000/users/SergeiZhuk/62"
response = requests.post(url_1)

if response.status_code == 200:
	print(response.json())
else:
	print(f"1 - Error: {response.text}")

url_2 = "http://127.0.0.1:8000/users/UrbanUser/24"
response = requests.post(url_2)

if response.status_code == 200:
	print(response.json())
else:
	print(f"2 - Error: {response.text}")
