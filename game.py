import re
from Board import Board, State


def choose_circle_position(board):
    xPosition = raw_input("Choose X position (0 - 2): ")
    yPosition = raw_input("Choose Y position (0 - 2): ")
    board[int(xPosition)][int(yPosition)] = 'O'


def choose_move():
    while True:
        x = raw_input("Choose X position (0-2): ")
        y = raw_input("Choose Y position (0-2): ")
        if not re.match("[0-2]", x) or not re.match("[0-2]", y):
            print 'Choose only 0, 1, or 2'
        else:
            break
    return int(x), int(y)


def main():
    boardObject = Board(3)
    newBoard = boardObject.create_board()
    x, y = choose_move()
    newBoard[x][y] = State.Cross
    boardObject.print_board(newBoard)


main()
