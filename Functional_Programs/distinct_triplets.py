from array import *
a=array('i',[ ])
n=int(input('Enter the number of elements-'))
for i in range(n):
    x=int(input('Enter the elements-'))
    a.append(x)
for i in range(0,n-2):
    c=0
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(a[i]+a[j]+a[k]==0):
                print(a[i],a[j],a[k])
                c=c+1
    print(c)