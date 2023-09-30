import requests

response = requests.get("https://habr.com/ru/articles/750312/")
print(response.text)
print(response.status_code)

