from board import Board
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"
        
    def start_game(self):
        # initializes players, board, and pieces
        self.board.initialize_pieces()
        self.board.create_board()

    def player_turn(self):
        #update piece position
        piece = self.board.get_piece_at(self.from_square)
        piece.position = self.to_square
        
        #update board
        self.board.update_board()
        
        #switch turns
        if self.turn == "WHITE":
            self.turn = "BLACK"
        else: 
            self.turn = "WHITE"

    def checkmate(self):
        return False

    def game_engine(self):
        if self.checkmate() == False:
            return True
        else:
            print(f"Checkmate! {self.turn} wins!")
            return False
        
    def valid_input(self, input_str):
        if len(input_str) == 2:
            if input_str[0].isalpha() and input_str[1].isdigit():
                return True
            else:
                print("Your input is invalid! Please try again.\n")
                return False
        else:
            print("Your input is invalid! Please try again.\n")
            return False
        
    def valid_piece(self):
        while True:
            piece_pos = input("Enter the square of your piece (e.g. 'e2'): ")
            
            if not self.valid_input(piece_pos):
                continue
            
            piece_color = self.board.get_piece_color(self.board.get_piece_at(piece_pos))
            
            if piece_color is None:
                print("There is no piece there! Please select one of your pieces.\n")
            elif piece_color != self.turn:
                print("This is not your piece. Please select one of your pieces.\n")
            else:
                return piece_pos

    def valid_destination(self, from_square):
        while True:
            to_square = input("Select a square to move to (e.g. 'e4'): ")
            
            if not self.valid_input(to_square):
                continue
            
            piece = self.board.get_piece_at(from_square)
            
            #validate move for piece
            if not self.is_valid_move(piece, from_square, to_square):
                print("Invalid move for this piece! Try again.\n")
                continue
            
            #check if your piece is occupying that square
            target_piece = self.board.get_piece_at(to_square)
            if target_piece is not None:
                if target_piece.color == piece.color:
                    print("Square is occupied by your own piece! Try again.\n")
                    continue
            
            return to_square

    def is_valid_move(self, piece, from_square, to_square):
        from_row, from_col = self.board.position_to_index(from_square)
        to_row, to_col = self.board.position_to_index(to_square)
        
        row_diff = to_row - from_row
        col_diff = to_col - from_col
        
        #piece movement validation
        if piece.name == "Pawn":
            return self.is_valid_pawn_move(piece, row_diff, col_diff)
        elif piece.name == "Rook":
            return self.is_valid_rook_move(row_diff, col_diff)
        elif piece.name == "Knight":
            return self.is_valid_knight_move(row_diff, col_diff)
        elif piece.name == "Bishop":
            return self.is_valid_bishop_move(row_diff, col_diff)
        elif piece.name == "Queen":
            return self.is_valid_queen_move(row_diff, col_diff)
        elif piece.name == "King":
            return self.is_valid_king_move(row_diff, col_diff)
        return False

    def is_valid_pawn_move(self, piece, row_diff, col_diff):
        if piece.color == "WHITE":
            return row_diff == -1 and col_diff == 0
        else:
            return row_diff == 1 and col_diff == 0

    def is_valid_rook_move(self, row_diff, col_diff):
        return (row_diff == 0 and col_diff != 0) or (col_diff == 0 and row_diff != 0)

    def is_valid_knight_move(self, row_diff, col_diff):
        return (abs(row_diff) == 2 and abs(col_diff) == 1) or (abs(row_diff) == 1 and abs(col_diff) == 2)

    def is_valid_bishop_move(self, row_diff, col_diff):
        return abs(row_diff) == abs(col_diff)

    def is_valid_queen_move(self, row_diff, col_diff):
        return self.is_valid_rook_move(row_diff, col_diff) or self.is_valid_bishop_move(row_diff, col_diff)

    def is_valid_king_move(self, row_diff, col_diff):
        return abs(row_diff) <= 1 and abs(col_diff) <= 1
    