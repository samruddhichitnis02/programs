import time
from array import *
import Utilities.algo_utility
sa = input('Press Enter to start the stopwatch')
print('Stopwatch started!')
begin = time.time()
a = [ ]
try:
    n = int(input('Enter the number of elements of String-'))
    for i in range(n):
        m=input('Enter the elements-')
        a.append(m)

    Utilities.algo_utility.bi_s(a)
    st = input('Press Enter to stop the stopwatch')
    print('Stopwatch stopped!')
    end = time.time()
    e = int(end - begin)
    print('The time elapsed is-', e, 'sec')
except:
    print('Length of string should be a digit!')