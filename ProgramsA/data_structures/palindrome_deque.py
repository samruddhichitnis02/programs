import sys
sys.path.append('../')
import Utilities
from Utilities import data
n=data.Deque()
a=input('Enter a String-')
b=a[: :-1]
n.addrear(a)
n.addfront(b)
n.check()