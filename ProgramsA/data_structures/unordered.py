import sys

sys.path.append('../')
import Utilities
from Utilities import data

x = []
l = data.Linked_list()

with open('abc.txt', 'r') as f:
    for line in f:
        for word in line.split():
            x.append(word)
            l.insert(word)
    l.print_list()

d = input('Enter the element to search in the list-')
l.search(x, d)