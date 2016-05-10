import requests
import sys
import json

# api_url = 'http://api.openweathermap.org/data/2.5/weather'

#city = input('City? ')

# params = {
#     'q': city,
#     'appid': '1dc3fdea9e4ffe3d0e39bababe43051d',
#     'units': 'metric'
# }
#
# res = requests.get(api_url, params=params)
# # print(res.status_code)
# # print(res.headers['Content-Type'])
# # print(res.text)
# data = res.json()   # returns json.loads(res.text)  :)
# template = 'Current temperature in {} is {}'
# print(template.format(city, data['main']['temp']))

#first task
sys.stdin = open("dataset_24476_3.txt", "r")


def number_true_task():
    for number in sys.stdin:
        api_url = 'http://numbersapi.com/' + number.rstrip() + '/math'
        params = {
            'json': 'true'
        }
        res = requests.get(api_url, params=params)
        data = res.json()
        if data['found']:
            print('Interesting')
        else:
            print("Boring")

#number_true_task()

# second task. Example working with developers.artsy.net

sys.stdin = open("input.txt", "r")
res = {}


def developers_artsy_net():
    client_id = '0c6388d1676572a87901'
    client_secret = '4dfc52d408b9d587bee6ef46fff1f86d'

    # инициируем запрос на получение токена
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

    # разбираем ответ сервера
    j = json.loads(r.text)

    # достаем токен
    token = j["token"]

    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token": token}

    for req in sys.stdin:
        api_url = "https://api.artsy.net/api/artists/" + req.rstrip()   # delete \n in end string

        # инициируем запрос с заголовком
        r = requests.get(api_url, headers=headers)

        # разбираем ответ сервера
        j = json.loads(r.text)
        if j['birthday'] not in res:
            year = int(j['birthday'])
            res[year] = []
            res[year].append(j['sortable_name'])
        elif j['birthday'] in res:
            year = int(j['birthday'])
            res[year].append(j['sortable_name'])

        print(res)
    # sort and output answer
    for key, value in sorted(res.items()):
        if len(value) > 1:
                value.sort()
        for i in value:
            print(i)

developers_artsy_net()