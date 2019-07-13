import sys
sys.path.append('../')
import Utilities.data
try:
    y=int(sys.argv[1])
    m=int(sys.argv[2])
    d = 1
    x=Utilities.data.cal(y,m,d)
    a = []
    for i in range(0, 7):
        a.append([])
    b = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
    for i in range(0, len(b)):
        a[i].append(b[i])

    if (((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0)):
        c = [32, 30, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]
    else:
        c = [32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]

    if (x == 0):
        j = 0
        for k in range(1, c[m - 1]):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    elif (x == 1):
        j = 1
        for k in range(1, c[m - 1]):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    elif (x == 2):
        j = 2
        for k in range(1, c[m - 1]):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    elif (x == 3):
        j = 3
        for k in range(1, c[m - 1]):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    elif (x == 4):
        j = 4
        for k in range(1, c[m - 1]):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    elif (x == 5):
        j = 5
        for k in range(1, c[m - 1]):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    elif (x == 6):
        j = 6
        for k in range(1, c[m - 1]):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0

    print(a)

except:
    print('Enter Valid Input!')