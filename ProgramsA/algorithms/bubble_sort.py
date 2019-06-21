from array import *
a=array('i',[ ])
n=int(input('Enter the no of elements in array-'))
for i in range(n):
	x=int(input('Enter the elements of array-'))
	a.append(x)
for i in range(n):
	for j in range(i+1,n):
		if(a[i]>a[j]):
			t=a[i]
			a[i]=a[j]
			a[j]=t
print(a)