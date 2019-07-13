import sys

sys.path.append('../')
import Utilities
from Utilities import data

try:
    l = data.Linked_List()
    fn = input('Enter the file name-')
    with open(fn, 'r') as f:
        for line in f:
            for word in line.split():
                # x.append(word)
                l.insert(word)
        l.print_list()
        print()
    f.close()

    a=input('Enter the element you want to search-')
    if(a.isalpha()):
        if(l.search(a)):
            l.delete_node(a)
            l.write_to_file()

        else:
            l.insert_at_end(a)
            l.write_to_file()
    else:
        print('Enter alphabets only!')
except:
    print('File not found!')