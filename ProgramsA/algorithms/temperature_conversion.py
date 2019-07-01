import Utilities.algo_utility
try:
    choice = int(input('Enter 1-to convert C to F OR 2- to convert from F to C 3- To exit:'))
    p=Utilities.algo_utility.temp_conversion(choice)
    print(p)
except:
    print('Enter digits only!')


