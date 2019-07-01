import Utilities.algo_utility
try:
    n=int(input('Enter a number-'))
    q=Utilities.algo_utility.tobinary(n)
except:
    print('Input a Number only!')