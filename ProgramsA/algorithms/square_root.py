import Utilities.algo_utility
try:
    c=int(input('Enter a number-'))
    a=Utilities.algo_utility.Root(c)
    print(a)
except:
    print('Enter Numbers only!')