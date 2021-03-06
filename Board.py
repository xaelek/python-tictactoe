from enum import Enum
from copy import deepcopy


class Board():

    def create_board(self, size):
        return [[State(State.Blank) for x in range(size)] for y in range(size)]

    def print_board(self, board):
        newBoard = deepcopy(board)
        for x in newBoard:
            if len(x) == 3:
                for y in x:
                    if y == State.Cross:
                        x[x.index(y)] = 'X'
                    if y == State.Blank:
                        x[x.index(y)] = ' '
                    if y == State.Circle:
                        x[x.index(y)] = 'O'
                print x


class State(Enum):
    Blank = 0
    Cross = 1
    Circle = -1
