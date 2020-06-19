
# Name:     Dan Wiltse
# Date:     11/3/2019
# Course:   DSC510
# Assign #: 10.1 Programming Assignment
# Purpose:   This program is designed to call the API for the Chuck Norris joke randomizer, then output the joke.
#            The user can request the program to run as many times as they like until they exit the program.


import requests

def get_joke():
 #get random jokes from url
  url = "https://api.chucknorris.io/jokes/random"
  response = requests.get(url)
  data = response.json()
  print(data["value"])
  print(response.status_code)     # To print http response code
  print("\n")


def main():
    # Greet user and explain purpose of program
    print('Welcome to my Chuck Norris joke randomizer!')
    print("\n")

 # Exitloop Variable to keep running loop until user exits out of it
    exitloop='N'

    while exitloop != 'Y':
        # Ask user if they want to hear a joke, otherwise they can exit by typing "exit" when done
        programtask = input('If you would like to hear a joke, type "Y" to continue or type "exit" to stop at anytime:')
        print("\n")
        #updating lower case to upper case for user input so both Y and y will run program
        if programtask.upper() == 'Y':
            get_joke()
            exitloop = 'N'
        #updating upper case to lower case for user input so both EXIT and exit will end the program
        elif programtask.lower() == 'exit':
            print('Thank you for using my joke randomizer, hope you enjoyed it. Goodbye!')
            # User ends loop by entering keyword "exit".
            exitloop = 'Y'
#Call main function created above
if __name__ == '__main__':
    main()
