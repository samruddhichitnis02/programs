try:
    import Utilities.utilities
    no=int(input('Enter the number of times you want to flip the coin-'))
    Utilities.utilities.flip(no)
except:
    print('Enter a number only!')