import sys
t=int(sys.argv[1])
v=int(sys.argv[2])
if(t<50 and v<120 and v>3):
	w=(35.74 + (0.6215*t) + ((0.4275*t) -35.75))* (pow(v,0.16))
	print(w)
elif(t>50 or v>120 or v<3):
	print('The value of Temperature should be above 50 and wind speed should be between 3-120  to calculate the windchill')