"""
   *************************
   **      Connect 4      **
   *************************

"""

# First player start with X
player = "  X  "

# Numbers of columns
columns = ["  1  ", "  2  ", "  3  ", "  4  ", "  5  ", "  6  ", "  7  "]

# Board empty slots
board = [
    ["     ", "     ", "     ", "     ", "     ", "     ", "     "],
    ["     ", "     ", "     ", "     ", "     ", "     ", "     "],
    ["     ", "     ", "     ", "     ", "     ", "     ", "     "],
    ["     ", "     ", "     ", "     ", "     ", "     ", "     "],
    ["     ", "     ", "     ", "     ", "     ", "     ", "     "],
    ["     ", "     ", "     ", "     ", "     ", "     ", "     "]
]

count = 0


# End the game
def end():
    print("Good Bye!")
    exit()


# If theres a winner, show who wins and ask to play again
def winner(piece):
    print(f"{piece} Wins")
    play_again = input("Want to play again? Y or N: ")
    if play_again.upper() == "Y" or play_again.upper() == "N":
        if play_again.upper() == "Y":
            for s in range(len(board)):
                for p in range(len(board[s])):
                    board[s][p] = "     "
            global count
            count = 0
            start(player)
        else:
            end()
    else:
        print("Please enter Y or N ...")
        winner(piece)


# Check for a winner
def check_for_winner(piece):
    # Check Horizontal
    for s in range(len(board)):
        for p in range(len(board[s]) - 3):
            if board[s][p] == piece and board[s][p + 1] == piece and board[s][p + 2] == piece and board[s][
                p + 3] == piece:
                return True

    # Check Vertical
    for s in range(3, len(board)):
        for p in range(len(board[s])):
            if board[s][p] == piece and board[s - 1][p] == piece and board[s - 2][p] == piece and board[s - 3][
                p] == piece:
                return True

    # Check positively sloped diaganols
    for s in range(len(board) - 3):
        for p in range(len(board[s]) - 3):
            if board[s][p] == piece and board[s + 1][p + 1] == piece and board[s + 2][p + 2] == piece and board[s + 3][
                p + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for s in range(3, len(board)):
        for p in range(len(board[s]) - 3):
            if board[s][p] == piece and board[s - 1][p + 1] == piece and board[s - 2][p + 2] == piece and board[s - 3][
                p + 3] == piece:
                return True


# Check is all the slot are full and no winner
def draw():
    print("Is a draw!")
    play_again = input("Want to play again? Y or N: ")
    if play_again.upper() == "Y" or play_again.upper() == "N":
        if play_again.upper() == "Y":
            for s in range(len(board)):
                for p in range(len(board[s])):
                    board[s][p] = "     "
            global count
            count = 0
            start(player)
        else:
            end()
    else:
        print("Please enter Y or N ...")
        draw()


# Start game - print board to screen
def start(piece, piece2=None):
    print("          ----------------------\n         |       Connect 4      |\n          ----------------------")
    print("\n", end="")
    for p in range(len(columns)):
        print("|" + columns[p], end="")
    print("|\n-------------------------------------------")
    for i in range(len(board)):
        for x in range(len(board[i])):
            print("|" + board[i][x], end="")
        print("|\n-------------------------------------------")
    if check_for_winner(piece2):
        winner(piece2)
    global count
    count += 1
    if count > 42:
        draw()
    else:
        user_input(piece)


# Check is the slot is empty to mark the piece into slot, else slot - 1
def play(i, x, piece):
    if board[i][x] == "     ":
        board[i][x] = piece
        piece2 = piece

        if piece != "  X  ":
            piece = "  X  "
            start(piece, piece2)
        else:
            piece = "  O  "
            start(piece, piece2)
    else:
        i -= 1
        play(i, x, piece)


# User input selector
def user_input(piece):
    try:
        input_num = int(input("Enter a column number: "))
        play(5, input_num - 1, piece)
    except OverflowError as err:
        print('Overflowed after ', err)
    except IndexError:
        print("Please enter a Number.")
        user_input(piece)
    except ValueError:
        print("Please enter a Number.")
        user_input(piece)


start(player)
