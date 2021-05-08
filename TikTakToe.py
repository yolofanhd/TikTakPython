import random

board = [0,0,0, 0,0,0, 0,0,0]

def init():
    printBoard()
    checkUserInput()

def printBoard():
    for i in range(len(board)):
        if (i+1)%3==0:
            print(board[i], '\n--------')
        else:
            print(board[i], '|', end='')
    checkBoard()

def checkUserInput():
    print("Please type in a number 1-9!")
    try:
        x = int(input())-1
        if x<0 or x>8 or board[x]!=0:
            return checkUserInput()
        board[x] = 'x'
        printBoard()
        makeTurn()
    except:
        exit()

def makeTurn():
    print("Computer is guessing...")
    x = random.randint(0,8)
    if board[x]!=0:
        return makeTurn()
    board[x]= '#'
    printBoard()
    checkUserInput()

def checkBoard():
    isFull = True
    for i in range(len(board)):
        if board[i] != 0:
            if(check(i)):
                if board[i] == 'x':
                    print("You won! :D")
                else:
                    print("You lost :c")
                exit()
        else:
            isFull = False
    if(isFull):
        print("Oh, nobody won!")
        exit()

def check(i):
    x = False
    if i%3==0 :
        x = board[i]==board[i+1] and board[i]==board[i+2]
    if not x and i<3:
        x = board[i]==board[i+3] and board[i]==board[i+6]
    if not x and i == 0:
        x = board[0]==board[4] and board[0]==board[8]
    if not x and i == 2:
        x = board[2]==board[4] and board[2]==board[6]
    return x

init()