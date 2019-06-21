from array import *
import time


class Utility():

    @staticmethod
    def i_i():
        sa = input('Press Enter to start the stopwatch')
        print('Stopwatch started!')
        begin = time.time()
        a = array('i', [])
        n = int(input('Enter the number of elements-'))
        for i in range(n):
            x = int(input('Enter the elements-'))
            a.append(x)
        for i in range(1, n):
            key = a[i]
            j = i - 1
            while (j >= 0 and key < a[j]):
                a[j + 1] = a[j]
                j = j - 1
            a[j + 1] = key
        print(a)
        st = input('Press Enter to stop the stopwatch')
        print('Stopwatch stopped!')

        end = time.time()

        e = int(end - begin)

        print('The time elapsed is-', e, 'sec')

    @staticmethod
    def b_i():
        sa = input('Press Enter to start the stopwatch')
        print('Stopwatch started!')
        begin = time.time()
        a = array('i', [])
        n = int(input('Enter the number of elements-'))
        for i in range(n):
            x = int(input('Enter the elements-'))
            a.append(x)
        for i in range(0, n):
            for j in range(i + 1, n):
                if (a[i] > a[j]):
                    t = a[i]
                    a[i] = a[j]
                    a[j] = t
        print(a)
        st = input('Press Enter to stop the stopwatch')
        print('Stopwatch stopped!')

        end = time.time()

        e = int(end - begin)

        print('The time elapsed is-', e, 'sec')

    @staticmethod
    def b_s():
        sa = input('Press Enter to start the stopwatch')
        print('Stopwatch started!')
        begin = time.time()
        def binary_search(a,low,high,y):
            if(high>=low):
                mid=low+((high-low)//2)
                if(a[mid]==y):
                    return mid
                elif (a[mid]>y):
                    return binary_search(a,low,mid-1,y)
                else:
                    return binary_search(a,mid+1,high,y)
            else:
                return -1

        a=array('i',[ ])
        n=int(input('Enter the number of elements-'))
        for i in range(n):
            x=int(input('Enter the elements-'))
            a.append(x)
        for i in range(0, n):
            for j in range(i + 1, n):
                if (a[i] > a[j]):
                    t = a[i]
                    a[i] = a[j]
                    a[j] = t
        y = int(input('Enter the element you want to search-'))
        z=binary_search(a,0,len(a)-1,y)
        if(z!=-1):
            print('The element you want is at position-',z)
        else:
            print('The element you want is not present in the array!')
        st = input('Press Enter to stop the stopwatch')
        print('Stopwatch stopped!')

        end = time.time()

        e = int(end - begin)

        print('The time elapsed is-', e, 'sec')

    @staticmethod
    def bi_s():
        sa = input('Press Enter to start the stopwatch')
        print('Stopwatch started!')
        begin = time.time()
        x = []
        n = input('Enter a String-')
        print(n)
        x = list(n)
        x.sort()
        m = ''.join(x)
        print(m)
        st = input('Press Enter to stop the stopwatch')
        print('Stopwatch stopped!')

        end = time.time()

        e = int(end - begin)

        print('The time elapsed is-', e, 'sec')


    @staticmethod
    def i_s():
        sa = input('Press Enter to start the stopwatch')
        print('Stopwatch started!')
        begin = time.time()
        x=[ ]
        n=input('Enter a String-')
        print(n)
        x=list(n)
        for i in range(1,len(x)):
            key=x[i]
            j=i-1
            while(j>=0 and key<x[j]):
                x[j+1]=x[j]
                j=j-1
            x[j+1]=key
        m=''.join(x)
        print(m)
        st = input('Press Enter to stop the stopwatch')
        print('Stopwatch stopped!')

        end = time.time()

        e = int(end - begin)

        print('The time elapsed is-', e, 'sec')

    @staticmethod
    def b_ss():
        sa = input('Press Enter to start the stopwatch')
        print('Stopwatch started!')
        begin = time.time()
        def binary_search(a, low, high, y):
            if (high >= low):
                mid = low + ((high - low) // 2)
                if (a[mid] == y):
                    return mid
                elif (a[mid] > y):
                    return binary_search(a, low, mid - 1, y)
                else:
                    return binary_search(a, mid + 1, high, y)
            else:
                return -1

        a = []
        n = input('Enter a String-')
        print(n)
        a = list(n)
        a.sort()
        m = ''.join(a)
        print(m)
        y = input('Enter the element you want to search-')
        z = binary_search(a, 0, len(a) - 1, y)
        if (z != -1):
            print('The element you want is at position-', z)
        else:
            print('The element you want is not present in the array!')
        st = input('Press Enter to stop the stopwatch')
        print('Stopwatch stopped!')

        end = time.time()

        e = int(end - begin)

        print('The time elapsed is-', e, 'sec')


while (True):

    choice = int(input('Choose 1- Insertion_Sort of Integers,2- Bubble_Sort of Integers,3-Binary_Search the Integers,4-Bubble Sort a String,5-Insertion Sort a String,6-Binary Search an element from string,0-Quit-'))
    if (choice == 1):
        Utility.i_i()
    elif (choice == 2):
        Utility.b_i()
    elif(choice==3):
        Utility.b_s()
    elif(choice==4):
        Utility.bi_s()
    elif(choice==5):
        Utility.i_s()
    elif(choice==6):
        Utility.b_ss()
    elif (choice == 0):
        break
    else:
        print('Invalid Choice')