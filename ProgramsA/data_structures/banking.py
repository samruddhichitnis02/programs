import sys
sys.path.append('../')
import Utilities
from Utilities import data
try:
    q=data.Queue()
    users=int(input('Enter the number of users-'))
    x=[ ]
    q.enqueue(users,x)
    amount = 0
    while(len(x)>0):
        choice = int(input('Enter 1 to deposit and 2 to withdraw the cash-'))
        if(choice==1):
            amt=int(input('Enter the amount to deposit-'))
            amount=amount+amt
            print('Amount  available in  bank',amount)
            q.dequeue(x)

        elif(choice==2):
            amt=int(input('Enter the amount to withdraw-'))
            amount=amount-amt
            print('Amount  available in  bank',amount)
            q.dequeue(x)
        continue

    if(amount==0):
        print('Balanced')
    else:
        print('Not balanced!')
except:
    print('Enter valid input!')

