import sys
sys.path.append('../') #appends the path of the required folder to import it
import Utilities
from Utilities import data
try:
	x=[ ]
	b=[ ]
	l=data.Link_list() #object Creation
	fn = input('Enter the file name-')
	with open(fn) as f:
		for line in f:
			for word in line.split(): #for every line in file split the words and append it to list
				x.append(word)
				for i in range(0, len(x)):
					x[i] = int(x[i])
				l.insert(word) #function calling
		l.print_list()
	l.order(x,b)
except:
	print('file not found!')