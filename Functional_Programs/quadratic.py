import math
a= int(input('Enter the coefficient of x-square-'))
b=int(input('Enter the coefficient of x-'))
c=int(input('Enter the constant value-'))
delta=(b*b)-(4*a*c)
r1=(-b + math.sqrt(delta))/(2*a)
r2=(-b - math.sqrt(delta))/(2*a)
print('Root 1 of equation is-',r1)
print('Root 2 of equation is-', r2)