
# Name:     Dan Wiltse
# Date:     11/17/2019
# Course:   DSC510
# Assign #: 12.1 Programming Assignment
# Purpose:   This program will allow a user to find information about the weather for a city by entering either the
#           name of city or its zip code, and then the program will call the information from an API back to the user.



import requests
#import pytemperature

url = "http://api.openweathermap.org/data/2.5/weather"

querystring = {"zip":"68116",
               "APPID": "f2a99365b7628b1ea22823fbcda4dd84"}

headers = {'cache=control':'no-cache'}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

#Create Main Program with Greeting that allows user to select which function to run
def main():
    # Greet user and explain purpose of program
    print('Welcome to my weather forecast program!')
    print("\n")

    # Exitloop Variable to keep running loop until user exits out of it
    exitloop='N'

    while exitloop != 'Y':
        # Ask user for which program they want to run, otherwise they can exit by typing "exit" when done
        print('Would you like to lookup eather data by US City or by Zip Code')
        programtask = input('Enter 1 for US City or 2 for zip code. Type "exit" to end the program: ')

        if programtask == '1':
            print('Current Weather conditions for Omaha:')

        pytemperature.k2f(temp) # Kelvin to Fahrenheit
        #Current Temp:
        #High Temp:
        #Low Temp:
        #Pressure:
        #Humidity
        #Cloud Cover
