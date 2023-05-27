import requests

answer = requests.get('https://www.pythoncheatsheet.org/')
print(answer.status_code)
print(answer.url)
print(answer.text)