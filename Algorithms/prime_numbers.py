n=1000
for  i in range(0,n):
	k=0
	for j in range(2,i//2+1):
		if(i%j==0):
			k=k+1
	if(k<=0):
		print(i,end=' ')