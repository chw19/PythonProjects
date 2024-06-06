

class ChessBoard:

    def __init__(self):
        self.board = self.create_board(row=8, col=8)

    def create_board(self, row, col):
        board = []
        for _ in range(row):
            current_row = []
            for _ in range(col):
                current_row.append(".")

            board.append(current_row)
        return board

    