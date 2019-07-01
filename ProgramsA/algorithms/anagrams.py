import Utilities.algo_utility
from array import *
n=input('Enter the  first string-')
m=input('Enter the second string-')
try:
    if(m.isalpha() and n.isalpha()):
        a = array('u', [])
        b = array('u', [])
        Utilities.algo_utility.ana(a,b,n,m)
    else:
        print('Enter alphabets only!')
except:
    print('Enter alphabets only!')