import Utilities.utilities

name = input('Enter the user name-')
try:
    if(name.isalpha()):
        print('The name is', name)
        Utilities.utilities.changed(name)
    else:
        print('Enter the name only no digits allowed!')
except:
    print('no digits allowed!')
