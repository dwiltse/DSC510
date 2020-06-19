def citystuff():
    import requests
    import pytemperature

    API_key = "f2a99365b7628b1ea22823fbcda4dd84"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = input("Enter City Name : ")

    Final_url = base_url + "appid=" + API_key + "&q=" + city_name
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
    low_temp = weather_data['main']['temp_min']

    # Accessing Longitude, it resides in coord and its key is lon
    high_temp = weather_data['main']['temp_max']

    # Printing Data


    #print(response.status_code)     # To print http response code
    print('Temperature : ',pytemperature.k2f(temp)) # Kelvin to Fahrenheit
    print('Low Temp: ',pytemperature.k2f(low_temp))
    print('High Temp : ',pytemperature.k2f(high_temp))
    print('Wind Speed : ',wind_speed)
    print('Description : ',description)


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
    low_temp = weather_data['main']['temp_min']

    # Accessing Longitude, it resides in coord and its key is lon
    high_temp = weather_data['main']['temp_max']

    # Printing Data


    #print(response.status_code)     # To print http response code
    print('Temperature : ',pytemperature.k2f(temp)) # Kelvin to Fahrenheit
    print('Low Temp: ',pytemperature.k2f(low_temp))
    print('High Temp : ',pytemperature.k2f(high_temp))
    print('Wind Speed : ',wind_speed)
    print('Current '
          'Description : ',description)

#Create Main Program with Greeting that allows user to select which function to run
def main():
    # Greet user and explain purpose of program
    print('Welcome to my weather program!')
    print("\n")

    # Exitloop Variable to keep running loop until user exits out of it
    exitloop='N'

    while exitloop != 'Y':
        # Ask user for which program they want to run, otherwise they can exit by typing "exit" when done
        programtask = input('Enter "city" for US City and "zip" for zip code. Type "exit" to end program:')
        if programtask.lower() == 'city':
            citystuff()
            exitloop = 'N'
        elif programtask.lower() == 'zip':
            zipstuff()
            exitloop = 'N'
        elif programtask == 'exit':
            print('Thank you for using my program, hope you enjoyed it. Goodbye!')
            # User ends loop by entering keyword "exit".
            exitloop = 'Y'
main()
