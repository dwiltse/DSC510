def zipstuff():
    import requests
    import pytemperature

    API_key = "f2a99365b7628b1ea22823fbcda4dd84"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    zip_code = input("Enter zip code : ")

    Final_url = base_url + "appid=" + API_key + "&q=" + zip_code
    try:
        response = requests.get(Final_url)
        weather_data = requests.get(Final_url).json()
        response.raise_for_status()
        print('Successful Process with', response.status_code)
    except requests.exceptions.HTTPError as e:
        print (e.response.text)

    # JSON data works just similar to python dictionary and you can access the value using [].
    # Accessing Temperature, temperature resides in main and its key is temp
    temp = weather_data['main']['temp']

    # Accessing wind speed, it resides in wind and its key is speed
    wind_speed = weather_data['wind']['speed']

    # Accessing Description, it resides in weather and its key is description
    description = weather_data['weather'][0]['description']

    # Accessing Latitude, it resides in coord and its key is lat
    latitude = weather_data['coord']['lat']

    # Accessing Longitude, it resides in coord and its key is lon
    longitude = weather_data['coord']['lon']

    # Printing Data


    #print(response.status_code)     # To print http response code
    print('Temperature : ',pytemperature.k2f(temp)) # Kelvin to Fahrenheit
    print('Wind Speed : ',wind_speed)
    print('Description : ',description)
    print('Latitude : ',latitude)
    print('Longitude : ',longitude)
