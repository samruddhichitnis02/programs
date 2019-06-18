import random
c1=0
c2=0
no=int(input('Enter the number of times you want to flip the coin-'))
if(no<0):
     print('Enter a positive number!')
else:
    for i in range(no):
        x=random.randint(0,1)
        print(x)
        if(x<0.5):
            c1=c1+1
        elif(x>0.5):
            c2=c2+1
n1=(c1/no)*100
print('The % of Tails is',n1,'%')
n2=(c2/no)*100
print('The % of Heads is',n2,'%')