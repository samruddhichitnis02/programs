N=int(input('Enter a number to print its harmonic-'))
if(N<=0):
	print('Number should be greater than zero')
else:
	H=1
	for i in range(2,N+1):
		H=H+1/i
	print('The Nth Harmonic value is-',H)