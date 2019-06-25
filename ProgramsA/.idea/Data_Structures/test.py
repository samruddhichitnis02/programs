x=[ ]
n=input('Enter a string')
for i in range(len(n)):
    x.append(n[i])
k=len(x)//2
print(x[:k])
print(x[k:])

