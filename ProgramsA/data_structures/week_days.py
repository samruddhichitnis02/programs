from array import *
a=array('u',[ ])
b=array('u',[ ])
n=input('Enter a String-')
for i in range(len(n)):
    a.append(n[i])
m=input('Enter a String-')
for i in range(len(m)):
    b.append(m[i])
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
for i in range(len(m)):
    for j in range(i+1,len(m)):
        if(b[i]>b[j]):
            t=b[i]
            b[i]=b[j]
            b[j]=t

c=0
if(len(a)==len(b)):
    for i in a:
        if i in b:
            c=c+1
if(c==len(a)):
    print('Anagrams')
else:
    print('Not Anagrams')