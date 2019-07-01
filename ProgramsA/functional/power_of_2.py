import sys
import Utilities.utilities
try:
    n=int(sys.argv[1])
    Utilities.utilities.power_of_2(n)
except:
    print('Enter a number only!')