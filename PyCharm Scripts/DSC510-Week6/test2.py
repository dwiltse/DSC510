lst = []
game_running = True
i=0
while 1:
    i+=1
    numbers = int(input('Enter number '))
    if numbers == -1:
        game_running = False
        break
lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
print('There are', len(lst), 'items in the list of temperatures')


