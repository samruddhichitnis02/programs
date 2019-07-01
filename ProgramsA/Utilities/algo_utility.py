def i_i(a,n): #method for insertion sort of integer
    for i in range(1, n):
        key = a[i] #get the largest value if present in current than previous in to key
        j = i - 1 #decrement the index of array
        while (j >= 0 and key < a[j]): #use while loop to check  if the array is sorted and if not sorted than swap
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    print(a)


def b_i(a,n): #function to bubble sort an integer
    for i in range(0, n): #get the index of an array
        for j in range(i + 1, n): #get the next index of the same array
            if (a[i] > a[j]): #compare the value of both the indices & swap if not sorted
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)


def binary_search(a,low,high,y): #function to binary search a string
    if(high>=low): #get the 1st & last values of the array
        mid=low+((high-low)//2) #take the middle element of the array
        if(a[mid]==y): #if the element is at midd pos than return the index of that element
            return mid
        elif (a[mid]>y): #if  The element is to the left of the array again take the 1st &last element  uptil mid element and check for the element to left of array
            return binary_search(a,low,mid-1,y)
        else: #check for the element to right of array
            return binary_search(a,mid+1,high,y)
    else:
        return -1






def bi_s(a): #Function to bubble sort a string
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] > a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)



def i_s(x): #function to insertion sort a string
    for i in range(1,len(x)):
        key=x[i]
        j=i-1
        while(j>=0 and key<x[j]):
            x[j+1]=x[j]
            j=j-1
        x[j+1]=key
    m=''.join(x)
    print(x)


def b_s(a, low, high, y): #function to binary search an integer
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
    for i in range(len(n)):#Enter the 1st string in array a
        a.append(n[i])
    for i in range(len(m)): #Enter the 2nd string in array b
        b.append(m[i])
    for i in range(len(n)): #Bubble sort the  1st array
        for j in range(i + 1, len(n)):
            if (a[i] > a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    for i in range(len(m)):#Bubble sort the 2nd array
        for j in range(i + 1, len(m)):
            if (b[i] > b[j]):
                t = b[i]
                b[i] = b[j]
                b[j] = t

    c = 0
    if (len(a) == len(b)):#if the length of both strings is same then they might be anagrams
        for i in a:
            if i in b: #check for each element in a if it is present in b
                c = c + 1#increment the count if element found
    if (c == len(a)): #if the count is equal to any of the length of string then it is an anagram
        print('Anagrams')
    else:
        print('Not Anagrams')

def prime_no(n):
    x=[ ]
    for i in range(2, n):
        k = 0
        for j in range(2, i // 2 + 1):#Use the floor division and add 1 to that value to get the range of j
            if (i % j == 0): #if i is divisible by j then increment k
                k = k + 1 #If k gets incremented for ith value then that ith value is not a prime number
        if (k <= 0):#if k's value is 0 for ith value then that number is prime number and that value is printed
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
        a = i #first take the element of ith position from array x and store it in a so that we can check it later to compare
        while (i > 0):
            r = i % 10 #divide the number by 10 and store the remainder in r
            rem = rem * 10 + r #reversing the number
            i = i // 10 #dividing the number to perform above operations again
        if (a == rem): #if the reversed number is equal to original number than its a palindrome
            y.append(a)
    print('The Palindrome numbers which are prime are-')
    return y

def anagrams(n):
    x = []
    z=[ ]
    for i in range(2, n):#first take the prime numbers in the range 1000
        k = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                k = k + 1
        if (k <= 0):
            x.append(i)
    print()
    print('The anagram numbers are-')
    m = ','.join(map(str, x))  # to convert list to string
    n = m.split(',')#to split various elements inside the list
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if (sorted(n[i]) == sorted(n[j])):
                z.append(n[i])
                z.append(n[j])
    return z

def bubble_s(a,n): #function to bubble sort the integer
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] > a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t
    print(a)

def vending(n,x,y):
    for i in range(0,len(x)):
        if(n>=x[i]):#if the amount entered is greater than or equal to any of the values present in x the amount can be divided by the value
            y[i]=n//x[i] #if the amount is divided then get the quotient of the division operation in y
            n=n-(y[i]*x[i]) #subtract the amount divided to get the remaining amount
    for i in range(len(y)):#If the ith index of y is not zero print i
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


def temp_conversion(choice):
    if (choice == 1):
        C = int(input('Enter the temperature in Celcius to convert to Farenhite-'))
        x = (C * (9 / 5)) + 32
        return x

    elif (choice == 2):
        F = int(input('Enter the temperature in Farenhite to convert to Celcius-'))
        y = (F - 32) * (5 / 9)
        return y

    elif (choice == 3):
        return

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


