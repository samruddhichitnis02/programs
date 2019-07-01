import os
import Utilities.algo_utility

a = []
try:
    fn=input('Enter the file name-')
    with open(fn) as f:
        for i in f:
            for j in i.split():
                a.append(j)
    print(a)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                t=a[i]
                a[i]=a[j]
                a[j]=t
    m = ''.join(a)
    print(m)
    y = input('Enter the element you want to search-')
    z = Utilities.algo_utility.binary_search(a, 0, len(a) - 1, y)
    if (z != -1):
        print('The element you want is at position-', z)
    else:
        print('The element you want is not present in the array!')

except:
    print('file does not exists!')




