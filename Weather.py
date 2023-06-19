from pprint import pprint
import requests
url='https://api.openweathermap.org/data/2.5/weather?units=metric&lat=12.9767936&lon=77.590082&appid=188a58f320824c5034d7a48080cd5e22'
res= requests.get(url)

data=res.json()
pprint(data)
temp= data['main']['temp']
print(temp)