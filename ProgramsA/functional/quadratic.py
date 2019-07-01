import Utilities.utilities
try:
    a=float(input('Enter the coefficient of x-square-'))
    b=float(input('Enter the coefficient of x-'))
    c=float(input('Enter the constant value-'))
    Utilities.utilities.quadratic(a,b,c)
except:
    print('All the three values of a,b,c should be a number!')