import Utilities.utilities
try:
    n=int(input('Enter the number of elements-'))
    Utilities.utilities.triplets(n)
except:
    print('Enter number only!')