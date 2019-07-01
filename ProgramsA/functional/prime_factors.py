import Utilities.utilities
try:
    n=int(input('Enter a number to print its prime factors-'))
    Utilities.utilities.factors(n)
except:
    print('Enter number only to know the prime factors!')