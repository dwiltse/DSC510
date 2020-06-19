'''
Your program must have a header. Use the programming style guide for guidance.
This program will perform various calculations (addition, subtraction, multiplication, division, and average calculation)
This program will contain a variety of loops and functions.
The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
Define a function named performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
This function will perform the given prompt the user for two numbers then perform the expected operation depending on the parameter that's passed into the function.
This function will print the calculated value for the end user.
Define a function named calculateAverage which takes no parameters.
This function will ask the user how many numbers they wish to input.
This function will use the number of times to run the program within a for loop in order to calculate the total and average.
This function will print the calculated average.
This program will have a main section which contains a while loop. The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
The main program should prompt the user for the operation they wish to perform.
The main program should evaluate the entered data using if statements.
The main program should call the necessary function to perform the calculation.
'''


# Name:     Dan Wiltse
# Date:     9/29/2019
# Course:   DSC510
# Assign #: 5.1 Programming Assignment
# Purpose:   This program is designed to allow a user to peform multiple calculations using loops within a function.
#           This will allow them to enter a number and find either the sum or dividend of the values, or the average
#           of included numbers, based on their input




#x = float(input("Enter a number (negative to quit) >> "))
#while x >= 0:

# Define our function
def performCalculation(operator):

#Ask user to enter in the two numbers you want to use in calculation
    value1= float(input('Enter the first number: '))
    value2 = float(input('Enter another number: '))

#Use if statement to decide which type of calculation to do based on parameter called below in function
    if operator == "+":
        output =  value1 + value2

    elif operator == "-":
         output = value1 - value2

    elif operator == "*":
         output = value1 * value2

    elif operator == "/":
         output = value1 / value2

    else:
        return "invalid operator"

#Call function with parameter to complete calculation depending on the operator typed in by user
print(performCalculation(input("Please enter the operator you would like to use (+,-, * or /): ")))



#Function to calculate sum and average of user entered numbers
def calculatedAverage():
    print('Average of ', num, ' numbers is :', avg)

num  = int(input('How many numbers: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
    avg = total_sum/num

print(calculatedAverage())

def main():
    # Welcome user, tell them what this program does
    # Eventually will hopefully be able to do some sort of real GUI :)
    print('|-------------------------------------|')
    print('|-----  Welcome to the program   -----|')
    print('|-- I will either perform a math -----|')
    print('|-- operation or calc an average -----|')
    print('|-------------------------------------|')

    # Initialize exitloop variable (n to stay in loop, y to end loop)
    exitloop='N'

    while exitloop != 'Y':
        # Ask user to enter one of three commands: calc an average, perform math operation, or exit
        print('Please enter keyword to perform task or exit.')
        tasktoperform = input('Valid values are MATH, AVERAGE, or QUIT: ')
        if tasktoperform == 'MATH':
            print('Ok, I will perform a mathematical operation for you.')
            operationtoperform = input('Please enter a mathematical operation to perform: + - * /')
            performCalculation(operationtoperform)
            exitloop = 'N'
        elif tasktoperform == 'AVERAGE':
            print('OK, I will ask you to enter some numbers and I will tell you the average.')
            calculateAverage()
            exitloop = 'N'
        elif tasktoperform == 'QUIT':
            print('Thank you for running this program, exiting now.  Have a great day!')
            # User wants to end program, set exitloop variable so loop ends.
            exitloop = 'Y'
        else:
            print('You did not enter a valid option, try again.')
            exitloop = 'N'


main()
