import requests

api_url = 'http://api.openweathermap.org/data/2.5/weather'

city = input('City? ')

params = {
    'q': city,
    'appid': '1dc3fdea9e4ffe3d0e39bababe43051d',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.text)
data = res.json()   # returns json.loads(res.text)  :)
template = 'Current temperature in {} is {}'
print(template.format(city, data['main']['temp']))

