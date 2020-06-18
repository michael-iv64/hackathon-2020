import requests
import json

url = 'https://api.hh.ru/vacancies'
params = {'area':1880}
response = requests.get(url, params=params)
response = response.json()
found = response['found']
f = open('text.json', 'w')
num = 0
while True:
    params['page'] = num
    num += 1
    response = requests.get(url, params = params)
    if response.status_code != 200:
            # if error
            print(r.json())
            break
    response = response.json()
    f.write(str(response) + '\n' + '\n')

