import requests
from pprint import pprint

API_key = "f2a99365b7628b1ea22823fbcda4dd84"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

zip_code = input("Enter a Zip code and country code : ")
Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code

weather_data = requests.get(Final_url).json


print("\nCurrent Weather Data Of " + zip_code +":\n")

pprint(weather_data)
 pip install CFBScrapy


