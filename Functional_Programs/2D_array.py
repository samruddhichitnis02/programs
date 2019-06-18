a=[ ]
m=int(input('Enter the number of rows-'))
n=int(input('Enter the number of coloumns-'))
for i in range(0,m):
    b=[ ]
    for j in range(0,n):
        c=int(input('Enter the values-'))
        b.append(c)
    a.append(b)
for i in range(0,m):
    for j in range(0,n):
        print(a[i][j],end=' ')
    print()