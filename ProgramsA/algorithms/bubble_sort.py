from array import *
import Utilities.algo_utility
a=array('i',[ ])
n=int(input('Enter the no of elements in array-'))
for i in range(n):
	x=int(input('Enter the elements of array-'))
	a.append(x)
Utilities.algo_utility.bubble_s(a,n)