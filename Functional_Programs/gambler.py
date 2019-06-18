import random
G=int(input('Enter  the amount you have-'))
S=int(input('Enter  the stake amount-'))
N=int(input('Enter the number of bets you want to make-'))
w=0
l=0
play='yes'
while (play == 'yes'):
    for i in range(N):
        R = random.randint(0, 2)
        if (R == 1):
            G = G + S
            w = w + 1
            print('You Won!')
            if (w > 0):
                break
        else:
            G = G - S
            l = l + 1
            print('You Lost!')

    play = input('Do you want to play again yes or no-')
if(w>=0):
	w=(w/N)  * 100
	print('lost %=',w)
	l=100-w
	print('winning %=', l)