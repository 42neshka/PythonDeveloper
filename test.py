
import requests
import datetime as dt

response = requests.get('http://wttr.in/?0T')
print(response.text)