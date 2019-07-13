import sys
sys.path.append('../') #appends the path of the required folder to import it
import Utilities
from Utilities import data
try:
	l = data.Linked_List()
	fn=input('Enter the file name-')
	with open(fn, 'r') as f:
		for line in f:
			for word in line.split():
				num = int(word)
				l.addNode(num)
	l.print_list()
	f.close()

	a = int(input('Enter the number you want to search-'))
	if (l.search(a)):
		l.delete_node(a)
		l.write_file()

	else:
		l.addNode(a)
		l.print_list()
		l.write_file()

except:
	print('file not found!')