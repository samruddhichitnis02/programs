x = []
y = []
z = []

# Prime Numbers in range0-1000
n = 1000
for i in range(0, n):
    k = 0
    for j in range(2, i // 2 + 1):
        if (i % j == 0):
            k = k + 1
    if (k <= 0):
        x.append(i)
print('The prime Numbers are-', x)
print()

# Prime Numbers which are Palindrome
for i in (x):
    rem = 0
    a = i
    while (i > 0):
        r = i % 10
        rem = rem * 10 + r
        i = i // 10
    if (a == rem):
        y.append(a)
print('The Palindrome numbers which are prime are-', y)
print()



print('The anagram numbers are-', z)


m=','.join(map(str,x)) #to convert list to string
n=str.split(m)
for i in range(len(n)):
   for j in range(i+1,len(n)):
       if(sorted(n[i]==n[j])):
           z.append(n[i])
           z.append(n[j])
print(z)