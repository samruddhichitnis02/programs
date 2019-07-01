import random
import sys
import string
import math
import time
import cmath
from array import *

def changed(name):
    if(len(name)>=3):
        new_name=input('Enter the new name to be replaced by old name-')
        n=name.replace(name,'Hello '+new_name+' How are you?')
        print(n)


def flip(no):
    c1 = 0 #count for tails
    c2 = 0 #count for heads
    if (no < 0):
        print('Enter a positive number!')
    else:
        for i in range(no):
            x = random.randint(0, 1) #randint generates a random integer from start to stop
            if (x < 0.5):
                c1 = c1 + 1
            elif (x > 0.5):
                c2 = c2 + 1
    n1 = (c1 / no) * 100 #formula to calculate % of tails
    print('The % of Tails is', n1, '%')
    n2 = (c2 / no) * 100 #formula to calculate % of heads
    print('The % of Heads is', n2, '%')


def leap(year):
    if (len(year) == 4):
        x = int(year) #convert the string to integer so that we can apply integer operations
        if (x % 4 == 0 and x % 100 != 0):
            print(year, ' is a leap year')
        elif (x % 400 == 0):
            print(year, ' is a leap year')
        else:
            print(year, ' is  not a leap year')
    else:
        print('Entered year does not have four digit!')

def power_of_2(n):
    if (n >= 0 and n < 31):
        for i in range(n, 31):
            x = 2 ** i  #exponent formula
            print(x)
    elif (n < 0):
        print('Enter a number greater than zero')
    elif (n > 31):
        print('Enter a number between 0-31')





def harmonic(N):
    if (N <= 0):
        print('Number should be greater than zero')
    else:
        H = 1 #value of 1st harmonic
        for i in range(2, N + 1):
            H = H + 1 / i #formula to get the harmonic of number greater than 1
        print('The Nth Harmonic value is-', H)


def factors(n):
    x=[ ]
    print('The prime factors of the given number are')
    for i in range(1, n + 1):
        if (n % i == 0): #if any number is divisible by n then append to list
            x.append(i)
    print(x)

def gambler(G,S,N):
    w = 0
    l = 0
    play = 'yes'
    while (play == 'yes'):#if the user wants to play then the loop will run
        for i in range(N):
            R = random.randint(0, 2)
            if (R == 1):
                G = G + S
                w = w + 1
                print('You Won!')
                if (w > 0): #if the player wins then break the loop
                    break
            else:
                G = G - S
                l = l + 1
                print('You Lost!')

        play = input('Do you want to play again yes or no-')
    if (w >= 0):
        w = (w / N) * 100
        print('winning %=', w)
        l = 100 - w
        print('lost %=', l)


def coupon(n):
    x = []
    y = []
    d = 0
    for i in range(n):
        z = random.randint(0, n + 1)
        x.append(z)
        d = d + 1 #Increment d for each times a random integer is generated
        if z not in y: #append only the unique values
            y.append(z)
    print('The distinct coupon numbers are-', y)
    print('Total distinct coupon numbers are',len(y),'and total random numbers  needed to have all distinct coupon numbers is-',d)

def dimension(m,n):
    a=[ ]
    for i in range(0,m):#no of rows
        b=[ ]
        for j in range(0,n): #no of coloumns
            c=input('Enter the values-')
            b.append(c)
        a.append(b)
    for i in range(0,m):
        for j in range(0,n):
            print(a[i][j],end=' ')
        print()


def triplets(n):
    a = array('i', [])
    for i in range(n):
        x = int(input('Enter the elements-'))
        a.append(x)
    for i in range(0, n - 2):
        c = 0 #count to get the number of distinct triplets
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k] == 0):
                    print(a[i], a[j], a[k])
                    c = c + 1
        print(c)


def distance(x,y):
    if (x >= 0 and y >= 0):
        dist = math.sqrt((pow(x, x)) + (pow(y, y)))
        print('The Euclidean Distance of the given point to the origin is-', dist)
    elif (x < 0 or y < 0):
        print('Enter positive number only!')

def stop(sa):
    if(sa=='S'):
        print('Stopwatch started!')
        begin = time.time()#returns the time from epoch up till now
        st = input('Press Enter to stop the stopwatch')
        print('Stopwatch stopped!')
        end = time.time()
        e = (end - begin)
        print('The time elapsed is=', e, 'sec')


def quadratic(a,b,c):
    delta = (b * b) - (4 * a * c)
    r1 = (-b + cmath.sqrt(delta)) / (2 * a)#cmath module gives the complex roots
    r2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print('Root 1 of equation is-', r1)
    print('Root 2 of equation is-', r2)

def wind_chill(t,v):
    if (t < 50 and v < 120 and v > 3):
        w = (35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75)) * (pow(v, 0.16))
        print(w)
    elif (t > 50 or v > 120 or v < 3):
        print(
            'The value of Temperature should be above 50 and wind speed should be between 3-120  to calculate the windchill')