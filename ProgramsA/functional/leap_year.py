import Utilities.utilities
try:
    year=input('Enter the year with four digits only-')
    Utilities.utilities.leap(year)
except:
    print('Enter a four digit number')
