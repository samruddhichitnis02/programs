x=[21,12,34,43,5,6]
y=[ ]
m=''.join(map(str,x))
print(m)
for i in range(len(m)):
    for j in range(i+1,len(m)):
        if(sorted(m[i])==sorted(m[j])):
            n=m[i],m[j]
            y=list(n)
            print(y)
