import Utilities.algo_utility
try:
    n=int(input('Enter the amount-'))
    x=[1000,500,100,50,10,5,2,1]
    y=[0,0,0,0,0,0,0,0,0]
    Utilities.algo_utility.vending(n,x,y)
except:
    print('Enter the amount in digits only!')