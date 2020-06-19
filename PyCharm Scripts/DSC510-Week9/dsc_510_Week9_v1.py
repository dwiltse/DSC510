'''
For this week we will modify our Gettysburg processing program from week 8 in order to generate a text file from the output rather than printing to the screen. Your program should have a new function called process_file which prints to the file (this method should almost be the same as the pretty_print function from last week. Keep in mind that we have print statements in main as well. Your program must modify the print statements from main as well.

Your program must have a header. Use the programming style guide for guidance.
Create a new function called process_fie. This function will perform the same operations as pretty_print from week 8 however it will print to a file instead of to the screen.
Modify your main method to print the length of the dictionary to the file as opposed to the screen.
This will require that you open the file twice. Once in main and once in process_file.
Prompt the user for the filename they wish to use to generate the report.
Use the filename specified by the user to write the file.
This will require you to pass the file as an additional parameter to your new process_file function.


'''
# Name:     Dan Wiltse
# Date:     10/27/2019
# Course:   DSC510
# Assign #: 9.1 Programming Assignment
# Purpose:   This program is designed to open a file containing the text of the Gettysburg address, load the individual
#            words into a dictionary and clean up the text to display a count of total words and count of individual
#            words that make up the dictionary. The user can choose the name of the file that this info will be exported into






#Create function that adds words from text to the dictionary
def add_word(word, dictionary):

    if word in dictionary:
        dictionary[word] += 1
    else:
        if len(word) !=0:
            dictionary[word] = 1

#Create function that processes each line in dictionary
def process_line(line, word_count_dict):

    import string
    string.punctuation
    '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    line = line.strip()
    word_list = line.split()

    for word in word_list:
        word = word.strip()
        word = word.translate(word.maketrans('', '', string.punctuation))
        word = word.lower()
        add_word(word, word_count_dict)

#Create function to format the final output from our code
def process_file(fnamer, word_count_dict):


    lst = list()
    for key, val in list(word_count_dict.items()):
        lst.append((val, key))

        lst.sort(reverse=True)
    #Append the dictionary info to the file with the count of letters

    with open(fnamer, 'a') as fileHandle:
        fileHandle.write ("\n")
        fileHandle.write('{:11s} {:11s}'.format('Word', 'Count'))
        fileHandle.write ("\n")
        fileHandle.write('-'*18)
        for key, val in lst:
            fileHandle.write('\n{:<11} {}'.format(val, key))


def main():
    #Create dictionary to insert gettysburg address
    word_count_dict = {}

    fname = input('Enter the full text file name you want to open (Ex - gettysburg.txt) : ')
    fnamer = input('Enter full file name you want to create (Ex - gettyexport.txt): ')


    try:
        gba_file = open(fname, 'r')
    except:
        print('File cannot be opened:', fname)
        exit()

    #Call function to update text in the dictionary
    for line in gba_file:
        process_line(line, word_count_dict)

    #Display the number of words in the final dictionary
    lenword = len(word_count_dict)
    with open(fnamer, 'w') as fileHandle:
         fileHandle.write("Length of Dictionary:  " + str(lenword))

    #Call function that formats the text and prints output
    #pretty_print(word_count_dict)

    process_file(fnamer, word_count_dict)



#Call main function created above
if __name__ == '__main__':
    main()

