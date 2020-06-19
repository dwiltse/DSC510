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
# Date:     9/22/2019
# Course:   DSC510
# Assign #: 4.1 Programming Assignment
#Purpose:   This program is designed to allow a user to enter their company name and amount of fiber optic cable needed
#           (in feet) in order to calculate the cost to install the requested amount of fiber optic cable. It will also
#           adjust the cost based on the bulk discount for amount needed over 100 feet. The input of feet needed and
#           cost based on bulk discount will be part of a function with multiple parameters.

 #Welcome statement to user
print('Welcome to my cable pricing calculator program!')
#Purpose statement
print('This program will allow a user to calculate the installation cost of fiber optic cable')
print("\n")
#Have user enter their company name
companyname = input('Please enter the name of your company?')

#Create function with multiple parameters
def MyFunction(feet, cableprice, bulkcost):
    print('Number of Feet of Cable Installed:', feet)
    print('Cost per foot (bulk discount over 100 feet):', bulkcost)
    print('Calculated Cost:', bulkcost,'*', feet, 'feet of cable =', cableprice, 'dollars')


#Input for feet parameter
feet = input('Please enter how many feet of fiber optic cable do you need?')

#Adding except to warn user to use numerical value in the feet parameter
try:
    feet = float(feet)
except:
    print('The number entered was not an integer. Please run the code again and enter a numerical value.')

#If statement for cableprice parameter calculation
if feet <=100:
    cableprice = round(float(feet)* float(0.87),2)
elif feet >100 and feet <=250:
    cableprice = round(float(feet)* float(0.80),2)
elif feet >250 and feet <=500:
    cableprice = round(float(feet)* float(0.70),2)
elif feet >500:
    cableprice = round(float(feet)* float(0.50),2)

#Parameter in function used for calculating the cost per foot to be used in receipt
if feet <=100:
    bulkcost = float(0.87)
elif feet >100 and feet <=250:
    bulkcost = float(0.80)
elif feet >250 and feet <=500:
    bulkcost = float(0.70)
elif feet >500:
    bulkcost = float(0.50)


#Section of code for output for receipt
print("\n")
print('Reciept for:', companyname)

#calling my function created above
MyFunction(feet, cableprice, bulkcost)
#final output line for receipt
print('The total fiber optic cable installation cost for',  companyname, 'for' ,feet,
      'feet of cable will be',  cableprice, 'dollars.')
