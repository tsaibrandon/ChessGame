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
        # self.start_position = []
    
    def initialize_pieces(self):
        # initializes pieces in their starting positions
        
        white_pieces = [
            Pawn(color = "WHITE", position = "a2"),
            Pawn(color = "WHITE", position = "b2"),
            Pawn(color = "WHITE", position = "c2"),
            Pawn(color = "WHITE", position = "d2"),
            Pawn(color = "WHITE", position = "e2"),
            Pawn(color = "WHITE", position = "f2"),
            Pawn(color = "WHITE", position = "g2"),
            Pawn(color = "WHITE", position = "h2"),
            Rook(color = "WHITE", position = "a1"),
            Rook(color = "WHITE", position = "h1"),
            Knight(color = "WHITE", position = "b1"),
            Knight(color = "WHITE", position = "g1"),
            Bishop(color = "WHITE", position = "c1"),
            Bishop(color = "WHITE", position = "f1"),
            Queen(color = "WHITE", position = "d1"),
            King(color = "WHITE", position = "e1")
        ]

        black_pieces = [
            Pawn(color = "BLACK", position = "a7"),
            Pawn(color = "BLACK", position = "b7"),
            Pawn(color = "BLACK", position = "c7"),
            Pawn(color = "BLACK", position = "d7"),
            Pawn(color = "BLACK", position = "e7"),
            Pawn(color = "BLACK", position = "f7"),
            Pawn(color = "BLACK", position = "g7"),
            Pawn(color = "BLACK", position = "h7"),
            Rook(color = "BLACK", position = "a8"),
            Rook(color = "BLACK", position = "h8"),
            Knight(color = "BLACK", position = "b8"),
            Knight(color = "BLACK", position = "g8"),
            Bishop(color = "BLACK", position = "c8"),
            Bishop(color = "BLACK", position = "f8"),
            Queen(color = "BLACK", position = "e8"),
            King(color = "BLACK", position = "d8")
        ]

        all_pieces = white_pieces + black_pieces

        for piece in all_pieces:
            self.place_piece(piece)

    def position_to_index(self, position):
        col = self.col_labels[position[0]]
        row = 8 - int(position[1])
        return row, col

    def place_piece(self, piece):
        row, col = self.position_to_index(piece.position)
        self.board[row][col] = piece.icon
        self.pieces.append(piece)
        # self.start_position.append(piece)

    def create_board(self):
        # prints out board in start state

        for row in self.board:
            print(" ".join(row))

    def update_board(self):
        # clears current board
        # updates the board after a move

        for i in range(8):
            for j in range(8):
                self.board[i][j] = "-"
        
        for piece in self.pieces:
            row, col = self.position_to_index(piece.position)
            self.board[row][col] = piece.icon
        
        self.create_board()