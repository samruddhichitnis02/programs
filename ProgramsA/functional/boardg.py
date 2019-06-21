board = [' ' for x in range(10)] #List comprehension



def insertLetter(letter,pos):
    # Insert the letter which is given as input to the position given as input
    board[pos]=letter

def spaceIsFree(pos):
    # If pos of board which we are giving is empty return True
    if(board[pos]==' '):
        return True
    else:
        return False

def printboard(board):
    # function to print the board
    print('   ', board[0], '|', board[1], '|', board[2])
    print('------|---|------')
    print('   ', board[3], '|', board[4], '|', board[5])
    print('------|---|------')
    print('   ', board[6], '|', board[7], '|', board[8])


def isWinner(bo,le):
    return((bo[1]==bo[2]==bo[3]==le) or #First row
    (bo[4] == bo[5] == bo[6] == le) or #2nd row
    (bo[7] == bo[8] == bo[9] == le) or #3rd row
    (bo[1] == bo[4] == bo[7] == le) or #1st coloumn
    (bo[2] == bo[5] == bo[8] == le) or #2nd coloumn
    (bo[3] == bo[6] == bo[9] == le) or#3rd coloumn
    (bo[1] == bo[5] == bo[9] == le) or #Diagonal
    (bo[3] == bo[5] == bo[7] == le)) #Diagonal


def playermove():#letter X
        t=True
        while t:
            a=int(input('Select a position where you want to place the desired choice-'))
            if(a<0 or a>9):
                print('Enter in  the range of 1-9')
            elif(a>0 and a<10):
                if spaceIsFree(a):
                    #If the pos we entered is free then stop this while loop
                    #and insert the X in the pos(a)
                    t=False
                    insertLetter('X',a)
                else:
                    print('The position you want is already occupied!')


def compMove():
    possible_moves=[x for x, letter in enumerate(board)  if letter==' ' and x!=0]
    move=0

    #Check using the below for loop that whether
    #Os can win or Xs can win
    for let in ['O','X']:
        #this for loop will give the positions left in the board
        for i in possible_moves:
            #This creates an another
            boardCopy = board[:]

def selectRandom(board):
    pass
def isBoardFull(board):
    #Return true if the board is full
    if(board.count(' ')>1):
        return False
    else:
        return True

def main():
    print('Welcome To the game!')
    printboard(board)
    while not (isBoardFull(board)):
        #when the board is not full then we perfrom the following operation=
        #The computer's move is O but if the computer didn't win then
        #it will go to the if  loop and ask the player to play & print the board
            if not (isWinner(board,'O')):
                playermove()
                printboard()
            else:
                print('Computer Won!')
                break

        # The computer's move is X but if the computer didn't win then
        # it will go to the if  loop and ask the comp to play & print the board
            if not (isWinner(board,'X')):
                move=compMove()
                if(move==0):
                    #if the computer is not able to move due to any reasons
                    #beacuse if there is no more moves for the computer to
                    #play then it must be a tie game
                    print('The game is a tie')
                else:
                    insertLetter('O',move)
                    print('Computer placed a O in position-',move)
                    printboard()
            else:
                print('Player Won!')
                break







    if  not isBoardFull(board):
        #If the board doesn't have an empty space then print
        print("Its' a tie!")

main()