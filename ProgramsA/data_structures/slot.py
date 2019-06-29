import sys
sys.path.append('../')
from Utilities import  data

s=data.Linked_slot()

x=[ ]
l0,l1, l2, l3, l4,l5,l6,l7,l8,l9,l10 = ([] for i in range(11))
with open('numbers.txt', 'r') as f:
    for line in f:
        for word in line.split():
            x.append(word)
            for i in range(len(x)):
                x[i] = int(x[i])

for i in(x):
    if(i%11==0):
        l0.append(i)
    elif(i%11==1):
        l1.append(i)
    elif (i % 11 ==2):
        l2.append(i)
    elif (i % 11 ==3):
        l3.append(i)
    elif (i % 11 ==4):
        l4.append(i)
    elif (i % 11 ==5):
        l5.append(i)
    elif (i % 11 ==6):
        l6.append(i)
    elif (i % 11 ==7):
        l7.append(i)
    elif (i % 11 ==8):
        l8.append(i)
    elif (i % 11 ==9):
        l9.append(i)
    elif (i % 11 ==10):
        l10.append(i)

for i in l0:
    s.insert(i)
print('0th slot is-')
s.print_list()
s.delete_list(l0)

for i in l1:
    s.insert(i)
print('1st slot is-')
s.print_list()
s.delete_list(l1)




for i in l2:
    s.insert(i)
print('2nd slot is-')
s.print_list()
s.delete_list(l2)

for i in l3:
    s.insert(i)
print('3rd slot is-')
s.print_list()
s.delete_list(l3)

for i in l4:
    s.insert(i)
print('4th slot is-')
s.print_list()
s.delete_list(l4)

for i in l5:
    s.insert(i)
print('5th slot is-')
s.print_list()
s.delete_list(l5)

for i in l6:
    s.insert(i)
print('6th slot is-')
s.print_list()
s.delete_list(l6)

for i in l7:
    s.insert(i)
print('7th slot is-')
s.print_list()
s.delete_list(l7)

for i in l8:
    s.insert(i)
print('8th slot is-')
s.print_list()
s.delete_list(l8)

for i in l9:
    s.insert(i)
print('9th slot is-')
s.print_list()
s.delete_list(l9)

for i in l10:
    s.insert(i)
print('10th slot is-')
s.print_list()
s.delete_list(l10)
j=s.search(x)

print(j)