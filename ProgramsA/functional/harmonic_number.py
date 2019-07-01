import Utilities.utilities
try:
    N=int(input('Enter a number to print its harmonic-'))
    Utilities.utilities.harmonic(N)
except:
    print('Enter number only!')