from copy import deepcopy
from Board import State
from Game import Game


class AI():

    def find_blanks(self, board):
        blanksBoard = deepcopy(board)
        for x in board:
            blanksBoard[blanksBoard.index(x)] = [i for i, y in enumerate(x) if y == State.Blank]
        return blanksBoard

    def find_next_move(self, board):
        blanksBoard = deepcopy(board)
        blanksBoard = AI.find_blanks(board)
        for x in blanksBoard:
            for y in x:
                return
