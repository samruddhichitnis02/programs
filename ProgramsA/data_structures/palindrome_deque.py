import sys
sys.path.append('../')
import Utilities
from Utilities import data
try:
    n=data.Deque()
    a=input('Enter a String-')
    if(a.isalpha()):
        b=a[: :-1]
        n.addrear(a)
        n.addfront(b)
        n.check()
    else:
        print('Enter a valid input!')
except:
    print('Enter a valid Input!')