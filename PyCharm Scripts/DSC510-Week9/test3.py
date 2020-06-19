
#Create function to export output to another file
def process_file(fname2, word_count_dict):
    lst = list()
    for key, val in list(word_count_dict.items()):
        lst.append((val, key))

        lst.sort(reverse=True)
    with open(fname2, 'w') as fileHandle:
        fileHandle.write('{:11s} {:11s}'.format('Word', 'Count'))
        fileHandle.write('-'*18)
        for key, val in lst:
            fileHandle.write('{:<11} {}'.format(val, key))
