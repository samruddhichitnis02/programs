import Utilities.utilities

a = [ ]
n = input('Enter a String-')
print(n)
a=list(n)
a.sort()
m=''.join(a)
print(m)
y = input('Enter the element you want to search-')
z = Utilities.utilities.binary_search(a, 0, len(a) - 1, y)
if (z != -1):
    print('The element you want is at position-', z)
else:
    print('The element you want is not present in the array!')
