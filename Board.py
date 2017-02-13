from enum import Enum


class Board():

    def create_board(self, size):
        return [[State() for x in range(size)] for y in range(size)]

    def print_board(self, board):
        for x in board:
            if len(x) == 3:
                print x


class State(Enum):
    Blank = 0
    Cross = 1
    Circle = -1
