# Name:     Dan Wiltse
# Date:     9/29/2019
# Course:   DSC510
# Assign #: 5.1 Programming Assignment
# Purpose:   This program is designed to allow a user to perform multiple calculations using loops within a function.
#           This will allow them to enter a number and find either the sum or dividend of the values, or the average
#           of included numbers, based on their input. Will allow user to select which function to run, and will
#           also use a loop to run until user exits the program.



# Define function for operator program to calculate two numbers based on operator selected
def performCalculation(operator):
        # Make sure the user enters one of the 4 operators below
    valid_operation = 'N'
    while valid_operation == 'N':
        if operator == '*':
            valid_operation = 'Y'
        elif operator == '+':
            valid_operation = 'Y'
        elif operator == '-':
            operator = 'Y'
        elif operator == '/':
            valid_operation = 'Y'
        else:
            operator = input('Invalid entry.  Please enter one of the four operators: + - * /:')

#Ask user to enter in the two numbers you want to use in calculation
    value1= float(input('Enter the first number: '))
    value2 = float(input('Enter another number: '))

#Use if statement to decide which type of calculation to do based on parameter called below in function
    if operator == "+":
        output = value1 + value2

    elif operator == "-":
        output = value1 - value2

    elif operator == "*":
        output = value1 * value2

    elif operator == "/":
        #if statement to deal with division by zero
        if value1 == 0 or value2 == 0:
            output = 0
        else:
            output = value1 / value2

    else:
        return "invalid operator"

#Call function with parameter to complete calculation depending on the operator typed in by user
    print(value1, operator,  value2, ' equals ', output)


#Function to calculate sum and average of user entered numbers
def calculateAverage():

#Ask user how many numbers to average. Force them to enter a number using try/except statement
    try:
        num = int(input('How many numbers would you like to input?'))
    except:
        num = int(input('How many numbers would you like to input?'))
#Create for loop to enter in the amount of numbers asked above and then average them
    total_sum = 0
    for n in range(num):
        numbers = float(input('Enter number : '))
        total_sum += numbers
        avg = total_sum/num
#Output for the AVERAGES PROGRAM
    print('You have entered ', num, ' numbers. The total sum is ', total_sum)
    print('The calculated average is: ', avg)


#Create Main Program with Greeting that allows user to select which function to run
def main():
    # Greet user and explain purpose of program
    print('Welcome to my computation program!')
    print("\n")

    # Exitloop Variable to keep running loop until user exits out of it
    exitloop='N'

    while exitloop != 'Y':
        # Ask user for which program they want to run, otherwise they can exit by typing "exit" when done
        print('Type "operator" to run a program that will add, subtract, divide or multiply any two numbers.')
        print('Type "averages" to run a program will allow you select how many numbers to calculate an average of their sum.')
        programtask = input('Please enter operator, averages, or exit: ')
        if programtask == 'operator':
            print('I will calculate any two numbers for you and let you pick what operator to use.')
            operator = input('Please enter a mathematical operation to perform: + - * /')
            performCalculation(operator)
            exitloop = 'N'
        elif programtask == 'averages':
            print('I will ask you to enter some numbers and I will tell you the average.')
            calculateAverage()
            exitloop = 'N'
        elif programtask == 'exit':
            print('Thank you for using my program, hope you enjoyed it. Goodbye!')
            # User ends loop by entering keyword "exit".
            exitloop = 'Y'
        else:
            print('You did not enter a valid option, try again.')
            exitloop = 'N'


main()
