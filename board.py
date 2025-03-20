from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Board:
    def __init__(self):
        self.board = [
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-"]
        ]
        
        self.col_labels = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7
        }
        
        self.pieces = []
    
    def initialize_pieces(self):
        for col_letter in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            self.place_piece(Pawn(color="WHITE", position=f"{col_letter}2"))
            
        for col_letter in ["a", "b", "c", "d", "e", "f", "g", "h"]:
            self.place_piece(Pawn(color="BLACK", position=f"{col_letter}7"))
        
        self.place_piece(Rook(color="WHITE", position="a1"))
        self.place_piece(Knight(color="WHITE", position="b1"))
        self.place_piece(Bishop(color="WHITE", position="c1"))
        self.place_piece(Queen(color="WHITE", position="d1"))
        self.place_piece(King(color="WHITE", position="e1"))
        self.place_piece(Bishop(color="WHITE", position="f1"))
        self.place_piece(Knight(color="WHITE", position="g1"))
        self.place_piece(Rook(color="WHITE", position="h1"))
        
        self.place_piece(Rook(color="BLACK", position="a8"))
        self.place_piece(Knight(color="BLACK", position="b8"))
        self.place_piece(Bishop(color="BLACK", position="c8"))
        self.place_piece(Queen(color="BLACK", position="d8"))
        self.place_piece(King(color="BLACK", position="e8"))
        self.place_piece(Bishop(color="BLACK", position="f8"))
        self.place_piece(Knight(color="BLACK", position="g8"))
        self.place_piece(Rook(color="BLACK", position="h8"))

    def position_to_index(self, position):
        col = self.col_labels[position[0]]
        row = 8 - int(position[1])
        return row, col

    def place_piece(self, piece):
        row, col = self.position_to_index(piece.position)
        self.board[row][col] = piece.icon
        self.pieces.append(piece)

    def create_board(self):
        print()
        
        for i, row in enumerate(self.board):
            print(f"{8-i}|{' '.join(row)}")
            
        print("  ---------------")
        print("  a b c d e f g h\n")


    def update_board(self):
        for i in range(8):
            for j in range(8):
                self.board[i][j] = "-"
        
        for piece in self.pieces:
            row, col = self.position_to_index(piece.position)
            self.board[row][col] = piece.icon
        
        self.create_board()
    
    def get_piece_at(self, position):
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None
            
    
    def get_piece_color(self, piece):
        if piece is not None:
            return piece.color
        return None