import time

sa=input('Press Enter to start the stopwatch')
print('Stopwatch started!')

begin=time.time()

st=input('Press Enter to stop the stopwatch')
print('Stopwatch stopped!')

end=time.time()

e=int(end-begin)

print('The time elapsed is-',e,'sec')
