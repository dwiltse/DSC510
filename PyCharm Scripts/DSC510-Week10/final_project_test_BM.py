# File: McDaniel_DSC510_FinalProj.py
# Name: Brian McDaniel
# Date: 11/15/2019
# Course: DSC510 Introduction to Programming, Section T303
# Desc: This program is an application that interacts with a webservice to obtain weather data.
#       It will prompt the user for their city or zip code and get data from OpenWeatherMap.
#       It will then display the weather information in a readable format to the user.
#
# Usage: This program calls a URL and returns a JSON file.  It prompts user to see if it should repeat functionality
'''
Weather Program
For your class project we will be creating an application to interacts with a webservice in order to obtain data.
Requirements:
Use Try blocks to ensure that your request was successful.
     If the connection was not successful display a message to the user.
Use try blocks when establishing connections to the webservice.
You must print a message to the user indicating whether or not the connection was successful
​
WEBSITE - https://openweathermap.org/appid
MY API KEY (REQUESTED ON 11/5/2019) - '7b705aefeed1c48ab795db1e79bc9c48'
                  retyping          - '7b705aefeed1c48ab795db1e79bc9c48'
                  key received via email on 11/5 at 11:42am
Username: brian.mcdaniel@outlook.com - Password: standard
'''
import requests
import json

def prettyprint(forecast):
    # Temporary code to test return of dictionary
    print('DEBUG__in prettyprint')
    print(forecast)

    print(forecast['main'])
    mainforecast = forecast['main']
    print(mainforecast)
    currenttemp = mainforecast['temp']
    lowtemp = mainforecast['temp_min']
    hightemp = mainforecast['temp_max']

    weatherforecast = forecast['weather']
    #description = weatherforecast['description']
    description = weatherforecast[0]['description']

    windforecast = forecast['wind']
    windspeed = windforecast['speed']

    cityname = forecast['name']

    # NOTE, May need to convert Kelvin to Fahrenheit
    # (0K − 273.15) × 9/5 + 32 = -459.7°F
    #  Another example, need to modify: fahrenTemp = (temp - 9/5) -459.67

    # Convert temperature from Kelvin to Fahrenheit
    currenttempf = (currenttemp - 273.15) * (9 / 5) + 32
    lowtempf = (lowtemp - 273.15) * (9 / 5) + 32
    hightempf = (hightemp - 273.15) * (9 / 5) + 32

    print('Here are the current weather conditions for {}:'.format(cityname))
    print('The current temperature is {}'.format(currenttempf))
    print('The low for today is {}'.format(lowtempf))
    print('the high for today is {}'.format(hightempf))
    print('The current conditions are {}'.format(description))
    print('The wind is currently blowing at {}'.format(windspeed))


def searchbyzip():
    print('DEBUG__You are in the searchbyzip function')

    # request and validate zip code
    validzipformat = 'N'
    while validzipformat == 'N':
        ziptosearch=input('Please enter the zip code to look up (5 digits): ')
        if (ziptosearch.isdigit()):
            # the user entered an integer, check for 5 digits
            if (len(ziptosearch) == 5):
                # entry is also 5 digits
                validzipformat = 'Y'
            else:
                print('Entered zip code is not 5 digits, please try again.')
                validzipformat = 'N'
        else:
            # user did not enter an integer
            print('Entered zip code is not an integer, please try again.')
            validzipformat = 'N'

    print('DEBUG___at this point, should have a valid zip: {}'.format(ziptosearch))
    print('DEBUG___Look up zip now')

    # build the URL for the call
    urltemp = 'http://api.openweathermap.org/data/2.5/weather?zip='
    apikey = '&APPID=7b705aefeed1c48ab795db1e79bc9c48'
    url = (urltemp + str(ziptosearch) + apikey)

    # perform the URL call and use try/catch logic
    response = requests.request("GET", url)
    fullforecast = json.loads(response.text)

    # return status of call and JSON
    return fullforecast


def searchbycity():
    print('DEBUG___You are in the searchbycity function')

    # request and validate city name
    validcityname = 'N'
    while validcityname == 'N':
        citytosearch=input('Please enter the name of the city to look up: ')
        print('DEBUG___city {}'.format(citytosearch))
        print('DEBUG___City name is entered')
        #    should I do some checking on city name?  Maybe check for non alpha characters?
        validcityname = 'Y'

    print('DEBUG___at this point, should have a valid city name: {}'.format(citytosearch))
    print('DEBUG___Look up city name now')

    # build the URL for the call
    urltemp = 'http://api.openweathermap.org/data/2.5/weather?q='
    apikey = '&APPID=7b705aefeed1c48ab795db1e79bc9c48'
    url = (urltemp + str(citytosearch) + apikey)

    # perform the URL call and use try/catch logic
    response = requests.request("GET", url)

    fullforecast = json.loads(response.text)
    print('DEBUG___printing full forecast next line')
    print(fullforecast)

    # return status of call and dictionary
    return fullforecast


def main():
    decoratorlinetop = '==========================================================='
    decoratorlinebody = '|                                                         |'

    print(decoratorlinetop)
    print('Welcome to my WEATHER PROGRAM!\n')
    print('You can enter a zipcode or a city and I will provide information for the weather in that location\n\n')
    print(decoratorlinetop)

    anotherlocation = 'Y'

    while anotherlocation.upper() == 'Y':

        # ask if they want to look up by city or zipcode
        print('Would you like to look up weather by a city name or a zipcode?')
        validchoice = False
        while validchoice == False:
            cityorzip = input('Please enter "city" or "zip": ')
            if cityorzip.upper() == 'CITY':
                print('You have chosen to look up weather by a city name.\n')
                validchoice = True
            elif cityorzip.upper() == 'ZIP':
                print('You have chosen to look up weather by a zip code.\n')
                validchoice = True
            else:
                print('Invalid entry, please try again.\n')
                validchoice = False

        # process look up by city name
        if cityorzip.upper() == 'CITY':
            print('DEBUG___City-Call module to look up city specific info, not passing in anything')
            forecast = searchbycity()

        # process look up by zip code
        if cityorzip.upper() == 'ZIP':
            print('DEBUG___Zip-Call module to look up zip code specific info, not passing in anything')
            forecast = searchbyzip()

        # read return code from the web call
        returnstatuscheck = str(forecast['cod'])
        print('DEBUG___Return code is below')
        print(returnstatuscheck)
        print(type(returnstatuscheck))
        # check for return code; 200 is success, 404 is not found, others?
        if returnstatuscheck == '404':
            # value note found
            print ('Location not found')
            errormessage = forecast['message']
            print(errormessage)
            print('Something went wrong on the lookup, please try again by answering Y to look up another location.\n')
        elif returnstatuscheck == '200':
            # success, normal processing
            # pretty print weather output
            print('DEBUG___call a pretty print function to format the JSON output, passing the JSON')
            prettyprint(forecast)
        else:
            # an unexpected error occurred
            print ('DEBUG___I did not expect this error...')
            errormessage = forecast['message']
            print(errormessage)

        # ask if they want to look up another location
        anotherlocation = input('\n\n Look up another location? (Enter "Y" for Yes)')
        print(decoratorlinetop)

    print('Thanks for using my WEATHER PROGRAM!')
    print(decoratorlinetop)

main()
