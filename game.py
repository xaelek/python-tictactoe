import re
from Board import Board, State


def choose_move(board):
    valid = True
    while valid:
        x = raw_input("Choose X position (0-2): ")
        y = raw_input("Choose Y position (0-2): ")
        if not re.match("[0-2]", x) or not re.match("[0-2]", y):
            print 'Choose only 0, 1, or 2'
        else:
            if board[int(x)][int(y)] == State.Blank:
                valid = False
            else:
                print 'That space is taken! Choose another position.'
    return int(x), int(y)


def check_win(board, x, y):
    if board[0][y] == board[1][y] == board[2][y]:
        return True
    if board[x][0] == board[x][1] == board[x][2]:
        return True
    if x == y and board[0][0] == board[1][1] == board[2][2]:
        return True
    if x + y == 2 and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def main():
    boardObject = Board()
    size = raw_input('Enter size of board to play: ')
    newBoard = boardObject.create_board(int(size))
    count = 0
    while True:
        x, y = choose_move(newBoard)
        count += 1
        if count % 2 == 0:
            newBoard[x][y] = State.Cross
            boardObject.print_board(newBoard)
            if check_win(newBoard, x, y):
                print 'Game winner for X!'
                break
        else:
            newBoard[x][y] = State.Circle
            boardObject.print_board(newBoard)
            if check_win(newBoard, x, y):
                print 'Game winner for O!'
                break
        if count == int(size) ** 2:
            print 'Game was a draw!'
            boardObject.print_board(newBoard)
            break


main()
