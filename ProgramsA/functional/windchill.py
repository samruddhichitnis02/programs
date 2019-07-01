import sys
import Utilities.utilities
try:
    t=int(sys.argv[1])
    v=int(sys.argv[2])
    Utilities.utilities.wind_chill(t,v)
except:
    print('Enter Digits only!')