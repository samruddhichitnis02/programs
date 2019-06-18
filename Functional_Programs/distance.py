import sys
import math
x=int(sys.argv[1])
y=int(sys.argv[2])
if(x>=0 and y>=0):
	dist=math.sqrt((pow(x,x))+(pow(y,y)))
	print('The Euclidean Distance of the given point to the origin is-',dist)
elif(x<0 or y<0):
	print('Enter positive numbers')