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

user_input -> specify what the user has to input,
user input should be a number between 1 and 9
(1 is the top left spot, and 9 is the right bottom spot)

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
    """
    Print out the board to the terminal. The function take board as the
    parameter. First, for every row the function iterates through
    each row in the board and then for each slot within every
    row it prints out a slot (which is a space where either an X,
    or an O can be placed during the game).
    The end parameter passed to the print function within the second for loop
    adds a whitespace to the end of each row. And for every row in the board
    each row will be printed on a new line.
    """
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()


print_board(board)

def quit(user_input):
    """
    The program quits if the user types in "q" as user input
    """
    if user_input == "q" or user_input == "Q":
        print("thanks for playing")
        return True
    else:
        return False

while True:
    """
    The while loop waits for input 
    """
    user_input = input("Please enter a position between 1 and 9, or enter 'q' to quit: ")
    if quit(user_input):
        break
    