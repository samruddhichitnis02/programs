import sys
import Utilities.algo_utility
try:
    P=int(sys.argv[1])
    Y=int(sys.argv[2])
    R=int(sys.argv[3])

    z=Utilities.algo_utility.Payment(P,Y,R)
    print('The payment is:',z)
except:
    print('Enter number only!')