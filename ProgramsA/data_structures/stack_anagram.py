import sys
sys.path.append('../')
import Utilities
from Utilities import data
s=data.Anagram()
x=[]
y=[]
n=1000
for i in range(2,n):
	k=0
	for j in range(2,i//2+1):
		if(i%j==0):
			k=k+1
	if(k<=0):
		x.append(i)

m=','.join(map(str,x))
a=m.split(',')
for i in range(len(a)):
	for j in range(i+1,len(a)):
		if(sorted(a[i])==sorted(a[j])):
			y.append(a[i])
			y.append(a[j])

s.create_stack(y)
s.pop()