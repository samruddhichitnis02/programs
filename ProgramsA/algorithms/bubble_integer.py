import time
import Utilities.algo_utility
from array import *
sa = input('Press Enter to start the stopwatch')
print('Stopwatch started!')
begin = time.time()
a = array('i', [])
n = int(input('Enter the number of elements-'))
for i in range(n):
    x = int(input('Enter the elements-'))
    a.append(x)
Utilities.algo_utility.b_i(a,n)
st = input('Press Enter to stop the stopwatch')
print('Stopwatch stopped!')
end = time.time()
e = int(end - begin)
print('The time elapsed is-', e, 'sec')

