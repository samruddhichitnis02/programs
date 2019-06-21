import time
import algorithms.utility
sa = input('Press Enter to start the stopwatch')
print('Stopwatch started!')
begin = time.time()
x = []
n = input('Enter a String-')
print(n)
x = list(n)
algorithms.utility.bi_s(x,n)
st = input('Press Enter to stop the stopwatch')
print('Stopwatch stopped!')
end = time.time()
e = int(end - begin)
print('The time elapsed is-', e, 'sec')