'''
Tic Tac Toe Game

Display the initial empty 3x3 board.
Ask the user to mark a square.
Computer marks a square.
Display the updated board state.
If it's a winning board, display the winner.
If the board is full, display tie.
If neither player won and the board is not full, go to #2
Play again?
If yes, go to #1
Goodbye!

'''


def display_board():
    '''
    Displays a 3x3 board
    '''
    board = ["" for _ in range(9)]
    print("|".join(board[:3]))
    print("-".join(board[3:7]))
    print("|".join(board[7:9]))
    print(board)
    board[0] = "X"
    print(board)


display_board()
def user_turn():
    '''
    '''

def computer_turn():
    '''
    
    '''

def check_winner():
    '''
    
    '''

def game():
    '''
    
    '''