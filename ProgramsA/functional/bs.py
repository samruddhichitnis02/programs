def binary_search(a, low, high, y):
    if (high >= low):
        mid = low + ((high - low) // 2)
        if (a[mid] == y):
            return mid
        elif (a[mid] > y):
            return binary_search(a, low, mid - 1, y)
        else:
            return binary_search(a, mid + 1, high, y)
    else:
        return -1


a = [ ]
n = input('Enter a String-')
print(n)
a=list(n)
a.sort()
m=''.join(a)
print(m)
y = input('Enter the element you want to search-')
z = binary_search(a, 0, len(a) - 1, y)
if (z != -1):
    print('The element you want is at position-', z)
else:
    print('The element you want is not present in the array!')
