class Queue:
    def __init__(self):
        self.x=[ ]

    def enqueue(self,users):
        for i in range(users):
            self.x.append(i)


    def dequeue(self):
        if(len(self.x)>0):
            self.x.pop()

    def cash(self):
        self.amount = 0
        while(len(self.x)>0):
            choice = int(input('Enter 1 to deposit and 2 to withdraw the cash-'))
            if(choice==1):
                amt=int(input('Enter the amount to deposit-'))
                self.amount=self.amount+amt
                print('Amount  available in  bank',self.amount)
                self.dequeue()

            elif(choice==2):
                amt=int(input('Enter the amount to withdraw-'))
                self.amount=self.amount-amt
                print('Amount  available in  bank',self.amount)
                self.dequeue()
            continue

        if(self.amount==0):
            print('Balanced')
        else:
            print('Not balanced!')



q=Queue()
users=int(input('Enter the number of users-'))
q.enqueue(users)
q.cash()
