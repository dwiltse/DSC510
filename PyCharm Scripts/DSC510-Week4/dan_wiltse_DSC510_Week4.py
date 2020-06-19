''''
This week we will modify our If Statement program to add a function to do the heavy lifting.
Modify your IF Statement program to add a function. This function will perform the cost calculation.
The function will have two parameters (feet and price). When you call the function, you will pass two arguments to the function;
 feet of fiber to be installed and the cost (remember that price is dependent on the number of feet being installed).

You probably should have the following:
Your program must have a header. Use the SIU Edwardsville Programming Guide for guidance.
A welcome message
A function with two parameters
A call to the function
The application should calculate the cost based upon the number of feet being ordered
A printed message displaying the company name and the total calculated cost
'''

# Name:     Dan Wiltse
# Date:     9/15/2019
# Course:   DSC510
# Assign #: 3.1 Programming Assignment
#Purpose:   This program is designed to allow a user to enter their company name and amount of fiber optic cable needed
#           (in feet) in order to calculate the cost to install the requested amount of fiber optic cable. It will also
#           adjust the cost based on the bulk discount for amount needed over 100 feet.




 #Welcome statement to user
print('Welcome to my cable pricing calculator program!')
#Purpose statement
print('This program will allow a user to calculate the installation cost of fiber optic cable')
print("\n")
#Collect company name and amount of cable needed from user using a function parameter

companyname = input('Please enter the name of your company?')
#have user input amount of cable
cablelength = input('Please enter how many feet of fiber optic cable do you need?')
#testing out the try statement to deal with non-numerical entries for cable length
try:
    cablelength = float(cablelength)
except:
    print('The number entered was not an integer. Please run the code again and enter a numerical value.')

#Calculate the cost of cable needed based on bulk discount. Rounding to 2 decimal places.
def MyFunction(feet, price):
    #print('Reciept for:', companyname)
    print('Number of Feet of Cable Installed:', cablelength)
    print('Cost per foot (bulk discount over 100 feet):', bulkcost)
    #print('Calculated Cost:', bulkcost,'*', cablelength, 'feet of cable =', cablecalculation, 'dollars')
    #print('The total fiber optic cable installation cost for',  companyname, 'for' ,cablelength,
    #  'feet of cable will be',  cablecalculation, 'dollars.')

    if cablelength <=100:
        cablecalculation = round(float(cablelength)* float(0.87),2)
    elif cablelength >100 and cablelength <=250:
        cablecalculation = round(float(cablelength)* float(0.80),2)
    elif cablelength >250 and cablelength <=500:
        cablecalculation = round(float(cablelength)* float(0.70),2)
    elif cablelength >500:
        cablecalculation = round(float(cablelength)* float(0.50),2)
#Calculating the cost per foot to be used in receipt below
    if cablelength <=100:
        bulkcost = float(0.87)
    elif cablelength >100 and cablelength <=250:
        bulkcost = float(0.80)
    elif cablelength >250 and cablelength <=500:
        bulkcost = float(0.70)
    elif cablelength >500:
        bulkcost = float(0.50)


#Final Output below
    print('Reciept for:', companyname)
    print('Number of Feet of Cable Installed:', cablelength)
    print('Cost per foot (bulk discount over 100 feet):', bulkcost)
    print('Calculated Cost:', bulkcost,'*', cablelength, 'feet of cable =', cablecalculation, 'dollars')
    print('The total fiber optic cable installation cost for',  companyname, 'for' ,cablelength,
      'feet of cable will be',  cablecalculation, 'dollars.')

MyFunction(cablelength2, bulkcost2)
