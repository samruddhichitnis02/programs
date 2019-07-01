import Utilities.utilities
try:
    m=int(input('Enter the number of rows-')) #No of rows
    n=int(input('Enter the number of coloumns-')) #No of coloumns
    Utilities.utilities.dimension(m,n)
except:
    print('Enter the integer values only!')