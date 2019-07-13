import sys
sys.path.append('../')
from Utilities import  data
y=[ ]

try:
    s=data.Linked_slot()
    s1=data.Linked_slot()
    s2 = data.Linked_slot()
    s3 = data.Linked_slot()
    s4 = data.Linked_slot()
    s5 = data.Linked_slot()
    s6 = data.Linked_slot()
    s7 = data.Linked_slot()
    s8 = data.Linked_slot()
    s9 = data.Linked_slot()
    s10=data.Linked_slot()

    x=[ ]
    with open('numbers.txt','r') as f:
        for line in f:
            for word in line.split():
                x.append(word)
            for i in range(len(x)):
                x[i] = int(x[i])

    for i in(x):
        if (i % 11 == 0):
            s.insert(i)
            y.append(s)
            s.print_list()
            s.delete_list()

        elif (i % 11 == 1):
            s1.insert(i)
            s1.print_list()
            y.append(s1)
            s1.delete_list()

        elif (i % 11 == 2):
            s2.insert(i)
            s2.print_list()
            y.append(s2)
            s2.delete_list()

        elif (i % 11 == 3):
            s3.insert(i)
            y.append(s3)
            s3.print_list()
            s3.delete_list()

        elif (i % 11 == 4):
            s4.insert(i)
            y.append(s4)
            s4.print_list()
            s4.delete_list()

        elif (i % 11 == 5):
            s5.insert(i)
            y.append(s5)
            s5.print_list()
            s5.delete_list()

        elif (i % 11 == 6):
            s6.insert(i)
            y.append(s6)
            s6.print_list()
            s6.delete_list()

        elif (i % 11 == 7):
            s7.insert(i)
            y.append(s7)
            s7.print_list()
            s7.delete_list()

        elif (i % 11 == 8):
            s8.insert(i)
            y.append(s8)
            s8.print_list()
            s8.delete_list()

        elif (i % 11 == 9):
            s9.insert(i)
            y.append(s9)
            s9.print_list()
            s9.delete_list()

        elif (i % 11 == 10):
            s10.insert(i)
            y.append(s10)
            s10.print_list()



    print(y)
    j=s.search(x)

    print(j)

except:
    raise ValueError
    #print('file not found!')