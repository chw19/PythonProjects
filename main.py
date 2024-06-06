import sys
sys.path.append('Classes')
from Classes.Board import ChessBoard

def main():

    chess_board = ChessBoard()

    for row in chess_board.board:
        print(''.join(row))

if __name__ =="__main__":
    main()

