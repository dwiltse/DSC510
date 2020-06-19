def performCalculation(operationtoperform):

    # Validate character passed into function.  If not (+,-,*,/) inform and loop to prompt for correct value
    valid_operation = 'N'
    while valid_operation == 'N':
        if operationtoperform == '*':
            valid_operation = 'Y'
        elif operationtoperform == '+':
            valid_operation = 'Y'
        elif operationtoperform == '-':
            valid_operation = 'Y'
        elif operationtoperform == '/':
            valid_operation = 'Y'
        else:
            operationtoperform = input('Invalid Operation entered, please enter one of the following: + - * /')

    # request and validate first number
    firstnumbervalid = 'N'
    while firstnumbervalid == 'N':
        firstnumber = input('Enter first number (positive integer please): ')
        if (firstnumber.isdigit()):
            # firstnumber is a positive integer!
            firstnumber = int(firstnumber)
            firstnumbervalid = 'Y'
        else:
           # firstnumber is NOT a positive integer!
            firstnumbervalid = 'N'

    # request and validate second number
    secondnumbervalid = 'N'
    while secondnumbervalid == 'N':
        secondnumber=input('Enter second number (positive integer please): ')
        if (secondnumber.isdigit()):
            # secondnumber is a positive integer!
            secondnumber = int(secondnumber)
            secondnumbervalid = 'Y'
        else:
            # secondnumber is NOT a positive integer!
            secondnumbervalid = 'N'

    # At this point, comfortable that operationtoperform and both numbers have been validated
    if operationtoperform == '*':
        mathoperationwording = ' multiplied by '
        mathoperationnoun = 'multiplication'
        operationresult = firstnumber * secondnumber
    elif operationtoperform == '+':
        operationresult = firstnumber + secondnumber
        mathoperationwording = ' added to '
        mathoperationnoun = 'addition'
    elif operationtoperform == '/':
        operationresult = firstnumber / secondnumber
        mathoperationwording = ' divided by '
        mathoperationnoun = 'division'
    elif operationtoperform == '-':
        operationresult = firstnumber - secondnumber
        mathoperationwording = ' subtracted from '
        mathoperationnoun = 'subtraction'

    # print a statement like " 1 divided by 2 is equal to .5"  phrasing set in contitional statement above
    print('You have entered two numbers and selected the math operation of ', mathoperationnoun)
    print(firstnumber, mathoperationwording, secondnumber, ' equals ', operationresult)


def calculateAverage():

    # request and validate how many numbers user wants to enter
    howmanynumbersinputvalid = 'N'
    while howmanynumbersinputvalid == 'N':
        howmanynumbers = input('How many numbers would you like to input?')
        if (howmanynumbers.isdigit()):
            # user entry is a positive integer!
            howmanynumbersinputvalid = 'Y'
            howmanynumbers = int(howmanynumbers)
        else:
            # user entry is NOT a positive integer!
            howmanynumbersinputvalid = 'N'

    totalamt = 0
    averageamt = 0
    for i in range(howmanynumbers):

        # FIRST, validate number
        inputnumbervalid = 'N'
        while inputnumbervalid == 'N':
            numberbeingrequested = i+1
            numrequestphrase = ('Enter number ' + str(numberbeingrequested) +':')
            inputnumber = input(numrequestphrase)
            if (inputnumber.isdigit()):
                # user entry is a positive integer!
                inputnumbervalid = 'Y'
                inputnumber = int(inputnumber)
            else:
                # user entry is NOT a positive integer!
                inputnumbervalid = 'N'

        # SECOND, increment the total amount
        totalamt = totalamt + inputnumber

    # THIRD, once through all the numbers, Calculate the Average
    averageamt = totalamt / inputnumber

    # FOURTH, print the average
    print('You have entered ', howmanynumbers, ' numbers.')
    print('The calculated average is: ', averageamt)


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
