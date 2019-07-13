import sys
sys.path.append('../')
import Utilities.utilities
try:
    n=int(input('Enter a  coupon number-'))
    Utilities.utilities.coupon(n)
except:
    print('Enter number only!')