
# Name:     Dan Wiltse
# Date:     11/17/2019
# Course:   DSC510
# Assign #: 12.1 Programming Assignment - Final Project
# Purpose:   This program will allow a user to find information about the weather for a city by entering either the
#           name of city or its zip code, and then the program will call the information from an API back to the user.



def citysearch():
    import requests
    import pytemperature
    #get URL for API call
    API_key = "f2a99365b7628b1ea22823fbcda4dd84"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = input("Enter City Name: ")
    print("\n")

    #perform API call and give status message depending if the entry is successful or not
    Final_url = base_url + "appid=" + API_key + "&q=" + city_name
    try:
        response = requests.get(Final_url)
        weather_data = requests.get(Final_url).json()
        response.raise_for_status()
        print('Successful City Name Search! (code =',response.status_code,')' )
    except requests.exceptions.HTTPError as e:
       # print (e.response.text)
        print("404-City Not Found")

        #run process if City is found
    if response.status_code != 404:

        # Accessing weather info like python dictionary in JSON using [] to call the value
        temp = weather_data['main']['temp']

        # pulling in wind speed, comes from wind section of API call
        wind_speed = weather_data['wind']['speed']

        # pulling in description of weather that comes from weather section of API call
        description = weather_data['weather'][0]['description']

        # pulling in low temp from main section of API call
        low_temp = weather_data['main']['temp_min']

        # pulling in high temp from main section of API call
        high_temp = weather_data['main']['temp_max']

        # Printing Data
        print("\n")
        print('Temperature: ',pytemperature.k2f(temp),'degrees') # Kelvin to Fahrenheit
        print('Low Temp: ',pytemperature.k2f(low_temp),'degrees')
        print('High Temp: ',pytemperature.k2f(high_temp),'degrees')
        print('Wind Speed: ',wind_speed,'mph')
        print('Current Description:',description)

    #Ask user to reinput request if  they enter an invalid city name
    else:
        print("Please try again with valid input. ")

def zipsearch():
    import requests
    import pytemperature

    API_key = "f2a99365b7628b1ea22823fbcda4dd84"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    zip_code = input("Enter a 5 digit US zip code: ")
    print("\n")
    #perform API call and give status message depending if the entry is successful or not
    Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code
    try:
        response = requests.get(Final_url)
        weather_data = requests.get(Final_url).json()
        response.raise_for_status()
        print('Successful Zip Code Search! (code =',response.status_code,')' )
    except requests.exceptions.HTTPError as e:
        #print (e.response.text)
        print("404-Zip Code Not Found")

    #process that runs if API call is successful
    if response.status_code != 404:

        # Accessing weather info like python dictionary in JSON using [] to call the value
        temp = weather_data['main']['temp']

        # pulling in wind speed, comes from wind section of API call
        wind_speed = weather_data['wind']['speed']

        # pulling in description of weather that comes from weather section of API call
        description = weather_data['weather'][0]['description']

        # pulling in low temp from main section of API call
        low_temp = weather_data['main']['temp_min']

        # pulling in high temp from main section of API call
        high_temp = weather_data['main']['temp_max']

        # Printing Data
        print("\n")
        print('Temperature: ',pytemperature.k2f(temp),'degrees') # Kelvin to Fahrenheit
        print('Low Temp: ',pytemperature.k2f(low_temp),'degrees')
        print('High Temp: ',pytemperature.k2f(high_temp),'degrees')
        print('Wind Speed: ',wind_speed,'mph')
        print('Current Description:',description)

    #Ask user to reinput request if  they enter an invalid zip code
    else:
        print("Please try again with valid input.")

#Create Main Program with Greeting that allows user to select which function to run
def main():
    # Greet user and explain purpose of program
    print('Welcome to my weather program! You can use it to search for a current forecast for any US City.')

    # Exitloop Variable to keep running loop until user exits out of it
    exitloop='N'

    while exitloop != 'Y':
        # Ask user for which program they want to run, otherwise they can exit by typing "exit" when done
        print("\n")
        programtask = input('Enter "city" for US City and "zip" for zip code. Type "exit" to end the program:')
        if programtask.lower() == 'city':
            citysearch()
            exitloop = 'N'
        elif programtask.lower() == 'zip':
            zipsearch()
            exitloop = 'N'
        elif programtask.lower() == 'exit':
            print("\n")
            print('Thank you for using my weather forecast program, hope you enjoyed it. Goodbye!')
            # User ends loop by entering keyword "exit".
            exitloop = 'Y'
main()
