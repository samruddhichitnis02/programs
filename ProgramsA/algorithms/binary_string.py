import Utilities.algo_utility
import time
sa = input('Press Enter to start the stopwatch')
print('Stopwatch started!')
begin = time.time()
a=[ ]
try:
    n = int(input('Enter length of String-'))
    for i in range(n):
        m=input('Enter the elements')
        if(m.isalpha()):
            a.append(m)
        else:
            print('enter valid input!')
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if(a[i]>a[j]):
                t=a[i]
                a[i]=a[j]
                a[j]=t
    m = ''.join(a)
    print(m)
    y = input('Enter the element you want to search-')
    z =Utilities.algo_utility.binary_search(a,0,len(a)-1,y)
    if (z != -1):
        print('The element you want is at position-', z)
    else:
        print('The element you want is not present in the array!')
    st = input('Press Enter to stop the stopwatch')
    print('Stopwatch stopped!')
    end = time.time()
    e = int(end - begin)
    print('The time elapsed is-', e, 'sec')

except:
    print('Enter valid Input!')


