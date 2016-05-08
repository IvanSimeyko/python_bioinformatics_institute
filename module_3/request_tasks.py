import requests

r = requests.get('http://ivansimeyko.com')   # простой get запрос
print(r.text)   # вывод ответа сервера