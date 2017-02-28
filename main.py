from Board import Board, State
from AI import AI
from Game import Game


def main():
    boardObject = Board()
    aiObject = AI()
    gameObject = Game()
    #size = raw_input('Enter size of board to play: ')
    size = 3
    newBoard = boardObject.create_board(int(size))
    count = 0
    while True:
        x, y = gameObject.choose_move(newBoard)
        count += 1
        if count % 2 == 0:
            newBoard[x][y] = State.Cross
            boardObject.print_board(newBoard)
            print aiObject.find_blanks(newBoard)
            if gameObject.check_win(newBoard, x, y):
                print 'Game winner for X!'
                break
        else:
            newBoard[x][y] = State.Circle
            boardObject.print_board(newBoard)
            print aiObject.find_blanks(newBoard)
            if gameObject.check_win(newBoard, x, y):
                print 'Game winner for O!'
                break
        if count == int(size) ** 2:
            print 'Game was a draw!'
            boardObject.print_board(newBoard)
            print aiObject.find_blanks(newBoard)
            break


main()
