import sys
import Utilities.data
try:
    y=int(sys.argv[1])
    m=int(sys.argv[2])
    z=[ ]
    z=Utilities.data.cal(y,m)
    print(z)
except:
    print('Enter Valid Input!')