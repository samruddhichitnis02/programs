x=[]
n=int(input('Enter a number to print its prime factors-'))
print('The prime factors of the given number are')
for i in range(1,n+1):
    if(n%i==0):
        x.append(i)
print(x)