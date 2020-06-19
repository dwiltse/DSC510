''''
Programming Assignment 1 (40 pts) Create a program with the following requirements
○ Using comments create a header at the top of the program indicating the purpose of the program, assignment number, and
your name. Use the SIUE Style Guide as reference: https://www.cs.siue.edu/programming-style-guide
○ Display a welcome message for your user.
○ Retrieve the company name from the user
○ Retrieve the number of feet of fiber optic cable to be installed from the user
○ Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $.87
○ Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total
cost in a legible format.
○ Include appropriate comments throughout the program
'''

# Name:     Dan Wiltse
# Date:     9/8/2019
# Course:   DSC510
# Assign #: 2.1 Programming Assignment
#Purpose:   This program is designed to allow a user to enter their company name and amount of fiber optic cable needed
#           (in feet) in order to calculate the cost to install the requested amount of fiber optic cable.




print('Welcome to my cable pricing calculator program!')  #Welcome statement to user
print('This program will allow a user to calculate the installation cost of fiber optic cable') #Purpose statement
print("\n")
companyname = input('Please enter the name of your company?')   #Collect company name from user
cablelength = input('Please enter how many feet of fiber optic cable do you need?') #have user input amount of cable
cablecalculation = float(cablelength)* float(0.87)  #Calculate amount of cable needed
print("\n")

#Final Output below
print('Reciept for:', companyname)
print('Number of Feet of Cable Installed:', cablelength)
print('Calculated Cost: $0.87 *', cablelength, 'feet of cable =', cablecalculation, 'dollars')
print('The total fiber optic cable installation cost for',  companyname, 'for' ,cablelength,
      'feet of cable will be',  cablecalculation, 'dollars.')


