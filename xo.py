board = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

turn = "X"  # X,O
is_finished = False # check finishing of game

print("Welcome to Tic Tac Toe v1.0.0")

while is_finished == False:
    # showing board
    print("========== Turn:", turn, "==========")
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])

    wich = input("Enter number of home: ")

    # check input - is standard?
    try:
        wich = int(wich)
    except:
        print("Your input isn't standard")
        continue

    # out of range error handeling
    while wich < 1 or wich > 9:
        print("Your number is out of range!")
        wich = input("Enter number of home: ")

        # check input
        try:
            wich = int(wich)
        except:
            print("Your input isn't standard")
            continue

    # check homes
    while board[wich - 1] == "X" or board[wich - 1] == "O":
        print("This home is full!")
        wich = input("Enter number of home: ")

        # check input
        try:
            wich = int(wich)
        except:
            print("Your input isn't standard")
        continue

    # set pieces and change it
    if turn == "X":
        board[wich - 1] = turn
        turn = "O"

    elif turn == "O":
        board[wich - 1] = turn
        turn = "X"

    # check winner
    if board[0] == board[1] == board[2]:
        print("==========", board[0], "Is Winner ==========")
        is_finished = True

    elif board[3] == board[4] == board[5]:
        print("==========", board[3], "Is Winner ==========")
        is_finished = True

    elif board[6] == board[7] == board[8]:
        print("==========", board[6], "Is Winner ==========")
        is_finished = True

    elif board[0] == board[3] == board[6]:
        print("==========", board[0], "Is Winner ==========")
        is_finished = True

    elif board[1] == board[4] == board[7]:
        print("==========", board[1], "Is Winner ==========")
        is_finished = True

    elif board[2] == board[5] == board[8]:
        print("==========", board[2], "Is Winner ==========")
        is_finished = True

    elif board[0] == board[4] == board[8]:
        print("==========", board[0], "Is Winner ==========")
        is_finished = True

    elif board[2] == board[4] == board[6]:
        print("==========", board[2], "Is Winner ==========")
        is_finished = True
    # check no winner
    elif board[0] != 1 and board[1] != 2 and board[2] != 3 and board[3] != 4 and board[4] != 5 and board[5] != 6 and \
            board[6] != 7 and board[7] != 8 and board[8] != 9:
        print("==========", "No Winner ==========")
        is_finished = True

# print final board
print(board[0], board[1], board[2])
print(board[3], board[4], board[5])
print(board[6], board[7], board[8])
