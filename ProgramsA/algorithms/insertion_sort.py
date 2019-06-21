
x = []
n = input('Enter a String-')
print(n)
x = list(n)
for i in range(1, len(x)):
	key = x[i]
	j = i - 1
	while (j >= 0 and key < x[j]):
		x[j + 1] = x[j]
		j = j - 1
	x[j + 1] = key
m = ''.join(x)
print(m)