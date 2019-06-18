import sys
n=int(sys.argv[1])
if(n>=0 and n<31):
	for i in range(n,31):
		x=2**i
		print(x)
elif(n<0):
	print('Enter a number greater than zero')
elif(n>31):
	print('Enter a number between 0-31')