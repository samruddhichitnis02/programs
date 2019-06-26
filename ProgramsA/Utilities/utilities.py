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
    else:
        print('Enter the name having minimum of three characters!')

def flip(no):
    c1 = 0
    c2 = 0
    if (no < 0):
        print('Enter a positive number!')
    else:
        for i in range(no):
            x = random.randint(0, 1)
            if (x < 0.5):
                c1 = c1 + 1
            elif (x > 0.5):
                c2 = c2 + 1
    n1 = (c1 / no) * 100
    print('The % of Tails is', n1, '%')
    n2 = (c2 / no) * 100
    print('The % of Heads is', n2, '%')


def leap(year):
    if (len(year) == 4):
        x = int(year)
        if (x % 4 == 0 and x % 100 != 0):
            print(year, ' is a leap year')
        elif (x % 400 == 0):
            print(year, ' is a leap year')
        else:
            print(year, ' is  not a leap year')
    else:
        print('Enter a four digit number')

def power_of_2(n):
    if (n >= 0 and n < 31):
        for i in range(n, 31):
            x = 2 ** i
            print(x)
    elif (n < 0):
        print('Enter a number greater than zero')
    elif (n > 31):
        print('Enter a number between 0-31')





def harmonic(N):
    if (N <= 0):
        print('Number should be greater than zero')
    else:
        H = 1
        for i in range(2, N + 1):
            H = H + 1 / i
        print('The Nth Harmonic value is-', H)


def factors(n):
    x=[ ]
    print('The prime factors of the given number are')
    for i in range(1, n + 1):
        if (n % i == 0):
            x.append(i)
    print(x)

def gambler(G,S,N):
    w = 0
    l = 0
    play = 'yes'
    while (play == 'yes'):
        for i in range(N):
            R = random.randint(0, 2)
            if (R == 1):
                G = G + S
                w = w + 1
                print('You Won!')
                if (w > 0):
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
        d = d + 1
        if z not in y:
            y.append(z)
    print('The distinct coupon numbers are-', y)
    print('Total distinct coupon numbers are',len(y),'and total random numbers  needed to have all distinct coupon numbers is-',d)

def dimension(m,n):
    a=[ ]
    for i in range(0,m):
        b=[ ]
        for j in range(0,n):
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
        c = 0
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
    print('Stopwatch started!')
    begin = time.time()
    st = input('Press Enter to stop the stopwatch')
    print('Stopwatch stopped!')
    end = time.time()
    e = (end - begin)
    print('The time elapsed is=', e, 'sec')


def quadratic(a,b,c):
    delta = (b * b) - (4 * a * c)
    r1 = (-b + cmath.sqrt(delta)) / (2 * a)
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


def ana(a,b):
    if (sorted(a) == sorted(b)):
        print('The  strings are anagrams')
    else:
        print('The strings are not anagrams')

def prime_no(n):
    x=[ ]
    for i in range(2, n):
        k = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                k = k + 1
        if (k <= 0):
            x.append(i)
    print(x)

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
    print('The Palindrome numbers which are prime are-', y)
    print()

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
    print('The anagram numbers are-')
    m = ','.join(map(str, x))  # to convert list to string
    n = m.split(',')
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if (sorted(n[i]) == sorted(n[j])):
                z.append(n[i])
                z.append(n[j])
    print(z)


