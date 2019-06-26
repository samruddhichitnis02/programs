import os
import Utilities.algo_utility
def fil():
    fn=input('Enter the file name-')
    if(os.path.isfile(fn)):
        f=open(fn)
        data=f.read()
        print(data)
        f.close()
        return data
    else:
        print('file does not exists!')





a = []
n=fil()
a = list(n)
a.sort()
m = ''.join(a)
print(m)
y = input('Enter the element you want to search-')
z = Utilities.algo_utility.binary_search(a, 0, len(a) - 1, y)
if (z != -1):
    print('The element you want is at position-', z)
else:
        print('The element you want is not present in the array!')



