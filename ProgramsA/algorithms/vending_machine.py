def Currency(n,x):
    for i in range(0,len(x)):
        if(n>=x[i]):
            y[i]=n//x[i]
            n=n-(y[i]*x[i])
    for i in range(len(y)):
        if(y[i]!=0):
            print(x[i],':',y[i])
n=int(input('Enter the amount-'))
x=[1000,500,100,50,10,5,2,1]
y=[0,0,0,0,0,0,0,0,0]
Currency(n,x)