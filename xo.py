board = [
    1,2,3,
    4,5,6,
    7,8,9
]

print("Welcome to Tic Tac Toe v1.0.0")

for i in range (9):
    print("------------------------")
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])
    wich = int(input("Enter number of home: "))
    while board[wich-1] == "X" or board[wich-1] == "O":
        print("This home is full!")
        wich = int(input("Enter number of home: "))
    if i % 2 == 0:
        board[wich-1] = "O"
    else:
        board[wich-1] = "X"
    
    if board[0] == board [1] == board[2]:
        print("------------------------")
        print(board[0]+" Is Wine!")
        break
    elif board[3] == board [4] == board[5]:
        print("------------------------")
        print(board[3]+" Is Wine!")
        break
    elif board[6] == board [7] == board[8]:
        print("------------------------")
        print(board[6]+" Is Wine!")
        break
    elif board[0] == board [3] == board[6]:
        print("------------------------")
        print(board[0]+" Is Wine!")
        break
    elif board[1] == board [4] == board[7]:
        print("------------------------")
        print(board[1]+" Is Wine!")
        break
    elif board[2] == board [5] == board[8]:
        print("------------------------")
        print(board[2]+" Is Wine!")
        break
    elif board[0] == board [4] == board[8]:
        print("------------------------")
        print(board[0]+" Is Wine!")
        break
    elif board[2] == board [4] == board[6]:
        print("------------------------")
        print(board[2]+" Is Wine!")
        break
print("------------------------")
print(board[0],board[1],board[2])
print(board[3],board[4],board[5])
print(board[6],board[7],board[8])
