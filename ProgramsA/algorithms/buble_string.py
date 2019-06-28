import time
from array import *
import Utilities.algo_utility
sa = input('Press Enter to start the stopwatch')
print('Stopwatch started!')
begin = time.time()
n = input('Enter a String-')
print(n)
a = array('u', [])
Utilities.algo_utility.bi_s(a,n)
st = input('Press Enter to stop the stopwatch')
print('Stopwatch stopped!')
end = time.time()
e = int(end - begin)
print('The time elapsed is-', e, 'sec')