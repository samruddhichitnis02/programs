import algorithms.utility
import time
a = []
sa = input('Press Enter to start the stopwatch')
print('Stopwatch started!')
begin = time.time()
n = input('Enter a String-')
print(n)
a = list(n)
a.sort()
m = ''.join(a)
print(m)
y = input('Enter the element you want to search-')
z = z=algorithms.utility.binary_search(a,0,len(a)-1,y)
if (z != -1):
    print('The element you want is at position-', z)
else:
    print('The element you want is not present in the array!')
st = input('Press Enter to stop the stopwatch')
print('Stopwatch stopped!')
end = time.time()
e = int(end - begin)
print('The time elapsed is-', e, 'sec')