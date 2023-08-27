board = "|1|2|3|\n|4|5|6|\n|7|8|9|"

def playerx(board):
    acceptablenumbers = range(1, 10)
    x = input("Player X, pick a number between 1 and 9: ")

    while not x.isdigit() or int(x) not in acceptablenumbers:
        print("Please insert a number from 1 to 9")
        x = input("Player X, pick a number between 1 and 9: ")

    newboard = board.replace(x, "X")
    print(newboard)
    return newboard

def playero(board):
    acceptablenumbers = range(1, 10)
    o = input("Player o, pick a number between 1 and 9: ")

    while not o.isdigit() or int(o) not in acceptablenumbers:
        print("Please insert a number from 1 to 9")
        o = input("Player o, pick a number between 1 and 9: ")

    newboard2 = board.replace(o, "O")
    print(newboard2)
    return newboard2

def changeboard(playerx, playero):

    global board
    print(board)
    board = playerx(board)
    board = playero(board)
    board = playerx(board)
    board = playero(board)
    board = playerx(board)
    board = playero(board)
    board = playerx(board)
    board = playero(board)
    board = playerx(board)
changeboard(playerx,playero)