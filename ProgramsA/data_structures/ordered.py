import sys
sys.path.append('../')
import Utilities
from Utilities import data
x=[ ]
b=[ ]
l=data.Link_list()
with open('pqr.txt','r') as f:
	for line in f:
		for word in line.split():
			x.append(word)
		for i in range(0, len(x)):
			x[i] = int(x[i])
		l.insert(word)
	l.print_list()
l.order(x,b)