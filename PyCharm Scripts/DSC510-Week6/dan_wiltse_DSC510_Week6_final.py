
# Name:     Dan Wiltse
# Date:     10/5/2019
# Course:   DSC510
# Assign #: 6.1 Programming Assignment
# Purpose:   This program is designed to allow a user to enter temperatures into a calculator to get min max and average
#            temperatures.  It will use a loop to run the program until the user enters a sentinel value to end the
#            program.



print('Hello, welcome to my temperature calculator!')
def main():
#Create empty list
    temperatures = list()
#Create while loop that runs unti sentinel value is entered by user
    while (True):
        inp = input('Enter a temperature (type exit when done entering numbers): ')
        if inp == 'exit': break
        value = float(inp)
        temperatures.append(value)
#if statement to deal with division by zero
        if sum(temperatures) == 0:
            average = 0
        else:
            average = sum(temperatures) / len(temperatures)
#print output below
    print('Average:', average)
    print('The largest temperature is :', max(temperatures),'degrees', '\nThe smallest temperature is:', min(temperatures) ,'degrees',)
    print('There are', len(temperatures), 'items in the list of temperatures')

if __name__ == '__main__':
    main()
