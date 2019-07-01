import Utilities.utilities
import sys
try:
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    Utilities.utilities.distance(x,y)
except:
    print('Enter number only!')