# Exitloop Variable to keep running loop until user exits out of it
exitloop='N'

while exitloop != 'Y':

        lst = []
        num = int(input('How many numbers (type end to stop entering numbers or type exit to end: '))
        if num != 'exit':
            for n in range(num):
                numbers = int(input('Enter number '))
                lst.append(numbers)
            print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
            print('There are', len(lst), 'items in the list of temperatures')
        elif num == 'exit':
            print('Thank you for using my program, hope you enjoyed it. Goodbye!')
            # User ends loop by entering keyword "exit".
            exitloop = 'Y'
