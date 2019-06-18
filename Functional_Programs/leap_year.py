import string
import math
year=input('Enter the year with four digits only-')
if(len(year)==4):
	x=int(year)
	if(x% 4==0 and x% 100!=0):
		print(year,' is a leap year')
	elif(x%400==0):
		print(year,' is a leap year')
	else:
		print(year,' is  not a leap year')
else:
	print('Enter a four digit number')