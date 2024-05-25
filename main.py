import random
board = ["-","-","-",
        "-","-","-",
         "-","-","-"]

currentplayer = "X"
Winner = None
gamerunning = True

def printBoard(board):
    print(board[0]+" | " +board[1] + " | "+board[2])
    print(board[3]+" | " +board[4] + " | "+board[5])
    print(board[6]+" | " +board[7] + " | "+board[8])




def playerInput(board):
    inp = int(input("Enter a Number 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("OOps place is already taken !")

def checkhorizontle(board):
    global Winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        Winner =board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        Winner =board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        Winner =board[6]
        return True
    

def checkrow(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        Winner =board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        Winner =board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        Winner =board[2]
        return True
    
def checkdiag(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        Winner =board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        Winner =board[2]
        return True
    
def checktie(board):
    global gamerunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gamerunning = False

def checkwin():
    if checkdiag(board) or checkhorizontle(board) or checkrow(board):
        print(f"the winner is {Winner}")

def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer="X"


def computer(board):
    while currentplayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] ="O"
            switchplayer()

while gamerunning:
    printBoard(board)
    playerInput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)
