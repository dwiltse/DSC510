
# Name:     Dan Wiltse
# Date:     11/10/2019
# Course:   DSC510
# Assign #: 11.1 Programming Assignment
# Purpose:   This program is designed to be a cash register to count the number of items and total value of items purchased


    #imports locale, which is used to set currency
import locale
    #setting locale used below
locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

    #Create Class
class CashRegister(object) :

    def __init__(self) :
        self.total_price = 0
        self.item_count = 0

#add items to cash register
    def add_item(self, price) :
        self.total_price += float(price)
        self.item_count += 1

#get total price of items
    def getTotal(self) :
        return self.total_price

#get count of items
    def getCount(self) :
        return self.item_count

#clear out info in Cash Register
    def clear(self) :
        self.item_count = 0
        self.total_price = 0.0


def main() :
    register = CashRegister()

    print('Welcome to my Cash Register Program!')
    print("\n")
    selection = True
    while selection:
            selection = input("If you would like to add an item to your cart, type Y, otherwise type N\n\t").upper()

            if selection == "Y" :
                price = input("What is the price of the item?\n\t")
                try:
                    register.add_item(price)
                except:
                    print('Please try again using a number')
            elif selection == 'N':
                #convert total cost to currency then print below
                grand_total = locale.currency(register.getTotal(), grouping=True)
                print('Total Cost: ', grand_total)
                print('Number of Items: ', register.getCount())
                print("\n")
                selection = False

    again=str(input("Do you want to use the register again? (Type yes to continue, no to end the program)"))
    #make sure that YES or yes will be accepted for input
    if again.lower() == 'yes':
        main()
    else:
        print('Thank you for shopping with us, come again!')

#Call main function created above
if __name__ == '__main__':
    main()


