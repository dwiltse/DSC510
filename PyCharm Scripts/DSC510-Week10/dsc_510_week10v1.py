import requests

url = "https://api.chucknorris.io/jokes/random"
#url = 'http://api.openweathermap.org/data/2.5/weather'

#querystring = {"value": ""}
querystring = {"zip":"68116",
               "APPID":"d5751b1a9e2e4b2b8c7983646072da8b"}

headers = {'cache-control': 'no cache'}

response = requests.request("GET", url, headers=headers)
print(response.text)
