import sys

y=int(sys.argv[1])
m=int(sys.argv[2])


a=[ ]
b=['Sun','Mon','Tue','Wed','Thur','Fri','Sat']
c=[31,28,31,30,31,30,31,31,30,31,30,31]


p=1
d=[ 0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

d0= int((y + y/4 - y/100 + y/400 + d[m-1] + p) % 7)


for i in range(0,7):
    a.append([ ])


for i in range(0,len(b)):
    a[i].append(b[i])


if((y%4==0 and y%100!=0) or (y%400==0)):
    c[1]=29



if (d0 == 0):
    j = 0
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        for k in range(1, 32):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    elif (m == 11 or m == 4 or m == 6  or m == 9 ):
        for k in range(1, 31):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0


elif (d0 == 1):
    j = 1
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        for k in range(1, 32):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    if (m == 11 or m == 4 or m == 6 or m == 9):
        for k in range(1, 31):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0



elif (d0 == 2):
    j = 2
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        for k in range(1, 32):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    if (m == 11 or m == 4 or m == 6 or m == 9):
        for k in range(1, 31):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0

elif (d0 == 3):
    j = 3
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        for k in range(1, 32):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    if (m == 11 or m == 4 or m == 6 or m == 9):
        for k in range(1, 31):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0

elif (d0 == 4):
    j = 4
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        for k in range(1, 32):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    if (m == 11 or m == 4 or m == 6 or m == 9):
        for k in range(1, 31):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0

elif (d0 == 5):
    j = 5
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        for k in range(1, 32):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    if (m == 11 or m == 4 or m == 6 or m == 9):
        for k in range(1, 31):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0


elif (d0 == 6):
    j = 6
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        for k in range(1, 32):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0
    if (m == 11 or m == 4 or m == 6 or m == 9):
        for k in range(1, 31):
            a[j].append(k)
            j = j + 1
            if (j == 7):
                j = 0


if(m==1):
    print('January',y)


elif(m==2):
    print('February',y)
elif(m==3):
    print('March',y)
elif(m==4):
    print('April',y)
elif(m==5):
    print('May',y)
elif(m==6):
    print('June',y)
elif(m==7):
    print('July',y)
elif(m==8):
    print('August',y)
elif(m==9):
    print('September',y)
elif(m==10):
    print('October',y)
elif(m==11):
    print('November',y)
else:
    print('December',y)

print(a)
print(d0)