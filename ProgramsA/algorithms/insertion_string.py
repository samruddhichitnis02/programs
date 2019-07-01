import time
import Utilities.algo_utility
sa = input('Press Enter to start the stopwatch')
print('Stopwatch started!')
begin = time.time()
x=[ ]
try:
    n = int(input('Enter the number of elements of String-'))
    for i in range(n):
       m=input('Enter the values-')
       x.append(m)
    Utilities.algo_utility.i_s(x)
    st = input('Press Enter to stop the stopwatch')
    print('Stopwatch stopped!')
    end = time.time()
    e = int(end - begin)
    print('The time elapsed is-', e, 'sec')

except:
    print('Enter valid inputs!')