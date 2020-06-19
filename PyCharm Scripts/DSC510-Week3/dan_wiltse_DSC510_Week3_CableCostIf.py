''''
This week we will implement “if statements” in a program. Your program will calculate the cost of fiber optic cable
installation by multiplying the number of feet needed by $0.87. We will also evaluate a bulk discount.
You will prompt the user for the number of fiber optic cable they need installed. Using the default value of $0.87
calculate the total expense. If the user purchases more than 100 feet they are charged $0.80 per foot. If the user
 purchases more than 250 feet they will be charged $0.70 per foot. If they purchase more than 500 feet,
 they will be charged $0.50 per foot.

Your program must have a header. Use the SUI--Edwardsville Programming Style Guide for guidance.
Display a welcome message for your program.
Get the company name from the user.
Get the number of feet of fiber optic cable to be installed from the user.
Evaluate the total cost based upon the number of feet requested.
Display the calculated information including the number of feet requested and company name.
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
#Collect company name from user
companyname = input('Please enter the name of your company?')
#have user input amount of cable
cablelength = input('Please enter how many feet of fiber optic cable do you need?')
#testing out the try statement to deal with non-numerical entries for cable length
try:
    cablelength = float(cablelength)
except:
    print('The number entered was not an integer. Please run the code again and enter a numerical value.')

#Calculate the cost of cable needed based on bulk discount. Rounding to 2 decimal places.
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

print("\n")

#Final Output below
print('Reciept for:', companyname)
print('Number of Feet of Cable Installed:', cablelength)
print('Cost per foot (bulk discount over 100 feet):', bulkcost)
print('Calculated Cost:', bulkcost,'*', cablelength, 'feet of cable =', cablecalculation, 'dollars')
print('The total fiber optic cable installation cost for',  companyname, 'for' ,cablelength,
      'feet of cable will be',  cablecalculation, 'dollars.')


