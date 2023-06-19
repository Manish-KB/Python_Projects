import datetime as dt
import requests


url="https://api.weatherapi.com/v1/current.json?key=6fa1106e16b7454cbae111911221210&q=Bengaluru"
response= requests.get(url).json()
print(response)

