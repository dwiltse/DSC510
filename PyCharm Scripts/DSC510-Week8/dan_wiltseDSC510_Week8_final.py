
# Name:     Dan Wiltse
# Date:     10/20/2019
# Course:   DSC510
# Assign #: 8.1 Programming Assignment
# Purpose:   This program is designed to open a file containing the text of the Gettysburg address, load the individual
#            words into a dictionary and clean up the text to display a count of total words and count of individual
#            words that make up the dictionary.


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
def pretty_print(word_count_dict):
    lst = list()
    for key, val in list(word_count_dict.items()):
        lst.append((val, key))

    lst.sort(reverse=True)
    print('{:11s} {:11s}'.format('Word', 'Count'))
    print('-'*18)
    for key, val in lst:
       print('{:<11} {}'.format(val, key))


def main():
    #Create dictionary to insert gettysburg address
    word_count_dict = {}

    #Open the file containing text
    gba_file = open('gettysburg.txt', 'r')

    #Call function to update text in the dictionary
    for line in gba_file:
        process_line(line, word_count_dict)

    #Display the number of words in the final dictionary
    print('Length of Dictionary: ', len(word_count_dict))


    #Call function that formats the text and prints output
    pretty_print(word_count_dict)

#Call main function created above
if __name__ == '__main__':
    main()
