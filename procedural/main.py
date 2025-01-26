import os 


board=["1","2","3",
       "4","5","6",
       "7","8","9"]
POSITIONS="123456789"
currentPlayer="X"
winner=None
gameRunning=True
# >1. printing the game board.
def printBoard(board):
    print(" "+board[0]+" | "+board[1]+" | "+board[2])
    print("---|---|---")
    print(" "+board[3]+" | "+board[4]+" | "+board[5])
    print("---|---|---")
    print(" "+board[6]+" | "+board[7]+" | "+board[8])
    

# >2. take player input.
def playerInput(board):
    global currentPlayer
    choice=int(input(f"\t it's {currentPlayer} turn.\n\t Enter a number 1-9: "))-1
    if 0<=choice<=8 and board[choice] in POSITIONS:
        board[choice]=currentPlayer 
    else:
        print("Invalid input. Try again.")
        playerInput(board)
        

# >3. check for win or tie.
def checkRows(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] not in POSITIONS:
        winner=board[0]
        return True
        # gameRunning=False 
    elif board[3] == board[4] == board[5] and board[4] not in POSITIONS:
        winner=board[3]
        return True
        # gameRunning=False
    elif board[6] == board[7] == board[8] and board[7] not in POSITIONS:
        winner=board[6]
        return True
        # gameRunning=False
def checkCols(board):
    global winner
    if   board[0] == board[3] == board[6] and board[0] not in POSITIONS:
        winner=board[0]
        return True
        # gameRunning=False
    elif board[1] == board[4] == board[7] and board[1] not in POSITIONS:
        winner=board[1]
        return True
        # gameRunning=False
    elif board[2] == board[5] == board[8] and board[2] not in POSITIONS:
        winner=board[2]
        return True
        # gameRunning=False
     
def checkDiagonal(board):
        global winner
        if   board[0] == board[4] == board[8] and board[0] not in POSITIONS:
            winner=board[0]
            return True
            # gameRunning=False
        elif board[2] == board[4] == board[6] and board[2] not in POSITIONS:
            winner=board[2]
            return True
            # gameRunning=False

def tie(board):
    global gameRunning
    if all(char not  in POSITIONS for char in board) and gameRunning  :
        printBoard(board)
        print("It's a tie!")
        gameRunning=False

def checkWin(board):
    global gameRunning
    if checkRows(board) or checkCols(board)or checkDiagonal(board):
        print(f"{winner} wins!")
        gameRunning=False
    else:
        tie(board)
    # if winner:
    #     printBoard(board)
    #     gameRunning=False
    
# >4. switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"
    
# >5. check for win or tie again.

# GAME Play:
while gameRunning:
    os.system("clear") if gameRunning else None
    printBoard(board)
    playerInput(board)
    checkWin(board)
    switchPlayer()

