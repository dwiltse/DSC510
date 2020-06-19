
operation = int(input("Which operatoin?"))


def performCalculation(operator):

#Ask user to enter in the two numbers you want to use in calculation
    value1= float(input('Enter the first number: '))
    value2 = float(input('Enter another number: '))

#Use if statement to decide which type of calculation to do based on parameter called below in function
    if operator == "+":
        return value1 + value2

    elif operator == "-":
        return value1 - value2

    elif operator == "*":
        return value1 * value2

    elif operator == "/":
        return value1 / value2

    else:
        return "invalid operator"

#Call function with parameter to complete calculation depending on the operator typed in by user
print(performCalculation(input("Please enter the operator you would like to use (+,-, * or /): ")))


while (operation >0):
    if operation == 1:
        return(performCalculation())
    elif operation == 2:
        print(calculateAverage())
    else:
        print('Have a nice day!')
