def i_i(a,n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while (j >= 0 and key < a[j]):
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    print(a)


def b_i(a,n):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (a[i] > a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)


def binary_search(a,low,high,y):
    if(high>=low):
        mid=low+((high-low)//2)
        if(a[mid]==y):
            return mid
        elif (a[mid]>y):
            return binary_search(a,low,mid-1,y)
        else:
            return binary_search(a,mid+1,high,y)
    else:
        return -1






def bi_s(a,n):

    for i in range(len(n)):
        a.append(n[i])
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] > a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)



def i_s(x):
    for i in range(1,len(x)):
        key=x[i]
        j=i-1
        while(j>=0 and key<x[j]):
            x[j+1]=x[j]
            j=j-1
        x[j+1]=key
    m=''.join(x)
    print(m)


def b_s(a, low, high, y):
    if (high >= low):
        mid = low + ((high - low) // 2)
        if (a[mid] == y):
            return mid
        elif (a[mid] > y):
            return b_s(a, low, mid - 1, y)
        else:
            return b_s(a, mid + 1, high, y)
    else:
        return -1

def ana(a,b,n,m):
    for i in range(len(n)):
        a.append(n[i])
    for i in range(len(m)):
        b.append(m[i])
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if (a[i] > a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    for i in range(len(m)):
        for j in range(i + 1, len(m)):
            if (b[i] > b[j]):
                t = b[i]
                b[i] = b[j]
                b[j] = t

    c = 0
    if (len(a) == len(b)):
        for i in a:
            if i in b:
                c = c + 1
    if (c == len(a)):
        print('Anagrams')
    else:
        print('Not Anagrams')

def prime_no(n):
    x=[ ]
    for i in range(2, n):
        k = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                k = k + 1
        if (k <= 0):
            x.append(i)
    return x

def palindrome(n):
    x = []
    y=[ ]
    for i in range(2, n):
        k = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                k = k + 1
        if (k <= 0):
            x.append(i)

    for i in (x):
        rem = 0
        a = i
        while (i > 0):
            r = i % 10
            rem = rem * 10 + r
            i = i // 10
        if (a == rem):
            y.append(a)
    print('The Palindrome numbers which are prime are-')
    return y

def anagrams(n):
    x = []
    z=[ ]
    for i in range(2, n):
        k = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                k = k + 1
        if (k <= 0):
            x.append(i)
    print()
    print('The anagram numbers are-')
    m = ','.join(map(str, x))  # to convert list to string
    n = m.split(',')
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if (sorted(n[i]) == sorted(n[j])):
                z.append(n[i])
                z.append(n[j])
    return z

def bubble_s(a,n):
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] > a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)

def vending(n,x,y):
    for i in range(0,len(x)):
        if(n>=x[i]):
            y[i]=n//x[i]
            n=n-(y[i]*x[i])
    for i in range(len(y)):
        if(y[i]!=0):
            print(x[i],':',y[i])

def day_week(d,m,y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7
    if (d0 == 0):
        print('Sunday')
    elif (d0 == 1):
        print('Monday')
    elif (d0 == 2):
        print('Tuesday')
    elif (d0 == 3):
        print('Wednesday')
    elif (d0 == 4):
        print('Thursday')
    elif (d0 == 5):
        print('Friday')
    else:
        print('Saturday')


def temp_conversion():
    while True:
        choice = int(input('Enter 1-to convert C to F OR 2- to convert from F to C 3- To exit:'))
        if (choice == 1):
            C = int(input('Enter the temperature in Celcius to convert to Farenhite-'))
            x = (C * (9 / 5)) + 32
            return x

        elif (choice == 2):
            F = int(input('Enter the temperature in Farenhite to convert to Celcius-'))
            y = (F - 32) * (5 / 9)
            return y

        elif (choice == 3):
            break

        elif (choice != 1 or choice != 2 or choice != 3):
            print('Invalid Choice')


def Payment(P,Y,R):
	n=12*Y
	r=R/(12*100)
	payment = (P*r)/(1-(1+r)**(-n))
	return payment


def Root(c):
    epsilon = 1e-15
    t = c
    while (abs(t - c / t) > epsilon * t):
        t = (c / t + t) / 2
    return t


def tobinary(n):
   x=[256,128,64,32,16,8,4,2,1]
   y=[0,0,0,0,0,0,0,0,0,0,0]
   for i in range(n):
       if(n>=x[i]):
           n=n-x[i]
           y[i].append(1)
       else:
           y[i].append(0)
    print(y)