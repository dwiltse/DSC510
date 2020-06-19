
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

#Create function to append the output to our text file
def process_file(fnamew, word_count_dict):


    lst = list()
    for key, val in list(word_count_dict.items()):
        lst.append((val, key))

        lst.sort(reverse=True)
    #Append the dictionary info to the file with the count of letters
    with open(fnamew, 'a') as fileHandle:
        fileHandle.write ("\n")
        fileHandle.write('{:11s} {:11s}'.format('Word', 'Count'))
        fileHandle.write ("\n")
        fileHandle.write('-'*18)
        for key, val in lst:
            fileHandle.write('\n{:<11} {}'.format(val, key))


def main():
    #Create dictionary to insert gettysburg address
    word_count_dict = {}

    #Ask user to load file name of gettysburg address
    fnamer = input('Enter the full text file name you want to open (Ex - gettysburg.txt) : ')

    #error handling if they enter the wrong file name
    try:
        gba_file = open(fnamer, 'r')
    except:
        print('File cannot be opened:', fnamer)
        exit()

    #ask user to create file where output is exported
    fnamew = input('Enter full file name you want to create (Ex - gettyexport.txt): ')

    #Call function to update text in the dictionary
    for line in gba_file:
        process_line(line, word_count_dict)

    #Display the number of words in the final dictionary and add them to text file created above in filenamew
    lenword = len(word_count_dict)
    with open(fnamew, 'w') as fileHandle:
         fileHandle.write("Length of Dictionary:  " + str(lenword))

    #Call function that formats the text and prints output
    #pretty_print(word_count_dict)

    process_file(fnamew, word_count_dict)



#Call main function created above
if __name__ == '__main__':
    main()

