"""
   *************************
   **      Connect 4      **
   *************************

"""

player = "  X  "

columns = ["  1  ", "  2  ", "  3  ", "  4  ", "  5  ", "  6  ", "  7  "]
board = [["     ", "     ", "     ", "     ", "     ", "     ", "     "], ["     ", "     ", "     ", "     ", "     ", "     ", "     "],
         ["     ", "     ", "     ", "     ", "     ", "     ", "     "], ["     ", "     ", "     ", "     ", "     ", "     ", "     "],
         ["     ", "     ", "     ", "     ", "     ", "     ", "     "], ["     ", "     ", "     ", "     ", "     ", "     ", "     "]]
count = 0


def end():
    print("Good Bye!")
    exit()


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
            table(player)
        else:
            end()
    else:
        print("Please enter Y or N ...")
        winner(piece)


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
    for s in range(len(board)):
        for p in range(len(board[s]) - 3):
            if board[s][p] == piece and board[s - 1][p + 1] == piece and board[s - 2][p + 2] == piece and board[s - 3][
                p + 3] == piece:
                return True


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
            table(player)
        else:
            end()
    else:
        print("Please enter Y or N ...")
        draw()


def table(piece, piece2=None):
    print("    ----------------------\n   |       Connect 4      |\n    ----------------------")
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
        start(piece)


def play(i, x, piece):
    if board[i][x] == "     ":
        board[i][x] = piece
        piece2 = piece

        if piece != "  X  ":
            piece = "  X  "
            table(piece, piece2)
        else:
            piece = "  O  "
            table(piece, piece2)
    else:
        i -= 1
        play(i, x, piece)


def start(piece):
    try:
        input_num = int(input("Enter a column number: "))
        play(5, input_num - 1, piece)
    except OverflowError as err:
        print('Overflowed after ', err)
    except IndexError:
        print("Please enter a Number.")
        start(piece)
    except ValueError:
        print("Please enter a Number.")
        start(piece)

table(player)
