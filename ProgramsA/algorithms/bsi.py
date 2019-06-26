from array import *
import Utilities.algo_utility
import time

sa = input('Press Enter to start the stopwatch')
print('Stopwatch started!')
begin = time.time()
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
z=Utilities.algo_utility.b_s(a,0,len(a)-1,y)
if(z!=-1):
    print('The element you want is at position-',z)
else:
    print('The element you want is not present in the array!')

st = input('Press Enter to stop the stopwatch')
print('Stopwatch stopped!')
end = time.time()
e = int(end - begin)
print('The time elapsed is-', e, 'sec')