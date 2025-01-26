import os 
os.system("clear")

class Board():
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        
    def __str__(self):
       return f"""
            | {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |
            |---|---|---|
            | {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |
            |---|---|---|
            | {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |
              
              """
b1=Board()

b1.board [0][0]="X"  

print(b1)
        

