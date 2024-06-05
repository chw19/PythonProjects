from PiecesInterface import Pieces

class Rook(Pieces):
    
    def __init__(self,color,piece_type):
        self.color = color
        self.piece_type = piece_type

    
    def move(self,start_pos,end_pos,board):
        
        start_row,start_col = start_pos
        end_row,end_col = end_pos

    #not a valid move     
        if end_row != start_row and end_col != start_col:
            return False
        
        if end_row != start_row:
            for _ in (start_row, end_row + 1):
                if board[_][start_col] is not None:
                    return False
            return True