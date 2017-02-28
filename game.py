import re
from Board import State


class Game():
    def choose_move(self, board):
        valid = True
        while valid:
            x = raw_input("Choose X position (0-2): ")
            y = raw_input("Choose Y position (0-2): ")
            if not re.match("^[0-2]$", x) or not re.match("^[0-2]$", y):
                print 'Choose only 0, 1, or 2'
            else:
                if board[int(x)][int(y)] == State.Blank:
                    valid = False
                else:
                    print 'That space is taken! Choose another position.'
        return int(x), int(y)

    def check_win(self, board, x, y):
        if board[0][y] == board[1][y] == board[2][y]:
            return True
        if board[x][0] == board[x][1] == board[x][2]:
            return True
        if x == y and board[0][0] == board[1][1] == board[2][2]:
            return True
        if x + y == 2 and board[0][2] == board[1][1] == board[2][0]:
            return True

        return False
