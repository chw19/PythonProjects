from PiecesInterface import Pieces


class Pawn(Pieces):
    
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    def move(self, start_pos, end_pos, board):
        
    #Determine direction of movement based off color
        
        direction = 0
        if self.color == 'white':
            direction += 1
        else:
            direction -= 1
    
    #Determine starting position & ending position

        start_row, start_col = start_pos
        end_row, end_col = end_pos

    #general movement

        if end_row == start_row + direction and start_col == end_col:
            if board[end_row][end_col] is None:
                return True
            
    #1st move
        starting_position = (self.color == 'white' and start_row == 1) or (self.color == 'black' and start_row == 6)

        if starting_position and end_row == 2 * direction and end_col == start_col:
            if board[end_row][end_col] is None and board[start_row + direction][start_col] is None:
                return True
            
    #Not valid move
        return False
    
    def capture(self, start_pos, end_pos, board):

        direction = 0
        if self.color == 'white':
            direction += 1
        else:
            direction -= 1

        start_row, start_col = start_pos
        end_row, end_col = end_pos

        if end_row == start_row + direction and abs(end_col - start_col) == 1:
            if board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
                return True

        return False 

    
    #Moving the Pawn on the Board from start position to end position

    def perform_move(self, start_pos, end_pos, board):

        if self.move(start_pos, end_pos, board) or self.capture(start_pos, end_pos, board):

            start_row, start_col = start_pos
            end_row, end_col = end_pos

            board[end_row][end_col] = self
            board[start_row][start_col] = None

        