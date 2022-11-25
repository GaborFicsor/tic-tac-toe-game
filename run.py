# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""
tic tac toe board
[
    [-,-,-],
    [-,-,-],
    [-,-,-],

]

possible challenges:
user want to go first, or let computer go first?

user_input -> specify what the user has to input, user input should be a number between 1 and 9 (1 is the top left spot, and 9 is the right bottom spot)

if they enter anything else: tell them to go again
check if user_input is already taken
add user_input to the board
check if user won: checking rows, columns and diagonals
toggle between users upon successfull moves
"""

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

print_board(board)