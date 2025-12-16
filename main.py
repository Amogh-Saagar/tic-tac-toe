import numpy as np

def printBoard(board):
    print(" |", "|".join(["———"]*3), "| ", sep = "")
    for row in board:
        print(" | ", " | ".join(row), " | ", sep = "")
        print(" |", "|".join(["———"]*3), "| ", sep = "")

def random(board, symbol):
    space = 0
    for row in board:
        space += row.count(" ")
    new = np.random.randint(1, space)
    counter = 1
    for x, row in enumerate(board):
        for y, ele in enumerate(row):
            if(ele == " "):
                if (new == counter):
                    board[x][y] = symbol
                    print(x, y)
                    return board
                counter+=1
            

def check(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]
    transpose = zip(row[0], row[1], row[2])
    for row in transpose:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]
    
    if(board[0][0] == board[1][1] == board[2][2] != " "):
        return board[0][0]
    
    if(board[2][0] == board[1][1] == board[0][2] != " "):
        return board[2][0]
    space = 0
    for row in board:
        space += row.count(" ")
    if space == 0:
        return "="
    return "-"

def play(board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]):
    running = 1
    player = input("Who do you wish to be, X or O: ").upper()
    if(player == "O"):
        computer = "X"
        random(board, computer)
    elif (player == "X"):
        computer = "O"
    else:
        print("Invalid input")
        return 
    while (running):
        printBoard(board)
        print("Enter location where you want to place: ")
        x = int(input("Enter row number (1, 2 or 3): "))
        y = int(input("Enter column number (1, 2 or 3): "))
        if(board[x-1][y-1] != " "):
            print("Please enter an empty space")
            continue
        board[x-1][y-1] = player
        current = check(board)
        if current == player:
            print("Congrats! Player wins!")
            return board
        elif current == "=":
            print("Its a draw")
            return board
        board = random(board, computer)
        current = check(board)
        if current == computer:
            print("Shucks! Computer wins!")
            return board
        elif current == "=":
            print("Its a draw")
            return board



board = play()
printBoard(board)
