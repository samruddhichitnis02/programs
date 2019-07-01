import Utilities.utilities
try:
    G=int(input('Enter  the amount you have-'))
    S=int(input('Enter  the stake amount-'))
    N=int(input('Enter the number of bets you want to make-'))
    Utilities.utilities.gambler(G,S,N)
except:
    print('Enter the number only for amount, stake amount, and number of bets!')