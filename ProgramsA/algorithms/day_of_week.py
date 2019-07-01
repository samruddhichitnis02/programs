import sys
import Utilities.algo_utility
try:
    d=int(sys.argv[1])
    m=int(sys.argv[2])
    y=int(sys.argv[3])
    Utilities.algo_utility.day_week(d,m,y)

except:
    print('Enter the days, month & year as a digit!')