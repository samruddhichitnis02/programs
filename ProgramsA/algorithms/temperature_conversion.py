class Temperature():
	@staticmethod
	def temp_conversion():
		while  True:
			choice=int(input('Enter 1-to convert C to F OR 2- to convert from F to C 3- To exit:'))
			if(choice==1):
				C=int(input('Enter the temperature in Celcius to convert to Farenhite-'))
				x=(C*(9/5))+32
				return x
			elif(choice==2):
				F=int(input('Enter the temperature in Farenhite to convert to Celcius-'))
				y=(F-32)*(5/9)
				return y
			elif(choice==3):
				break
			elif(choice!=1 or choice !=2 or choice!=3):
				print('Invalid Choice')


p=Temperature.temp_conversion()
print(p)