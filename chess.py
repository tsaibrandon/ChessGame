class Chess:
    """
        This engine of the game. Where all the basic rules are kept to make sure the game runs properly.
    """
    def __init__(self):
        self.turn = 1
        self.board = Board()
        

    def game_engine(self):
        # if it is not checkmate then the game continues
        # if checkmate detected then game ends

        return True

    def start_game(self):
        # initializes players, board, and pieces

        self.board.initialize_pieces()
        self.board.create_board()

        while self.game_engine():
            self.player_turn()
            self.end_game()

    def player_turn(self):
        # gets players input for pieces to move where 
        
        selected_square = input(
            f"It's {self.check_turn()}'s turn!\n"
            "Enter the square of the piece would you like to move: "
        )
        
        self.is_valid_piece(selected_square)

        move_to_square = input(
            "Enter the square you would like to move your piece to: "
        )

        self.move_piece(selected_square, move_to_square)

    def check_turn(self):
        # returns who's turn it is

        if self.turn == 1:
            return "WHITE"
        else:
            return "BLACK"

    def cordinate_to_index(self, selected_square):
        # changes user input to array notation

            col = selected_square[0]
            col = self.board.col_labels[col]
            row = 8 - int(selected_square[1])
            return row, col
    
    def is_valid_piece(self, selected_square):
        # checks to see if that is a piece that the player can move

        piece = self.square_occupied_by(selected_square)

        if self.check_turn() == "WHITE":
            if piece is not None and piece.color == "WHITE":
                print("ok")
                self.turn += 1
                return "VALID"
            elif piece is not None and piece.color == "BLACK":
                print("Not valid piece")
                self.player_turn()
                return "NOT VALID"
            else:
                print("There is no piece there! Try again.")
                self.player_turn()
                return "NOT VALID"
        else:
            if piece is not None and piece.color == "BLACK":
                print("ok")
                self.turn -= 1
                return "VALID"
            elif piece is not None and piece.color == "WHITE":
                print("Not valid piece")
                self.player_turn()
                return "NOT VALID"
            else:
                print("There is no piece there! Try again.")
                self.player_turn()
                return "NOT VALID"

    def square_occupied_by(self, selected_square):
        # checks if there is a piece on that square
        # checks what colored piece is on that square

        row, col = self.cordinate_to_index(selected_square)

        if self.board.board[row][col] != "-":
            for piece in self.board.pieces:
                if piece.position == selected_square:
                    return piece
        else:
            return None

    def move_piece(self, selected_square, move_to_square):
        # moves the selected piece

        if self.is_valid_move(selected_square, move_to_square) == "VALID":
            self.update_piece_position(selected_square, move_to_square)
            self.board.update_board()
        else:
            print("Invalid square! Please select another.")

    def is_valid_move(self, selected_square, move_to_square):
        # based on what piece is selected check to see if the piece can be moved to said square

        piece = self.square_occupied_by(selected_square)
        row, col = self.cordinate_to_index(selected_square)

        if piece.name == "Pawn":
            if piece.pawn_valid_move(selected_square, move_to_square) == "VALID":
                return "VALID"
        elif piece.name == "Rook":
            pass
        elif piece.name == "Knight":
            pass
        elif piece.name == "Bishop":
            pass
        elif piece.name == "Queen":
            pass
        else:
            pass

    def update_piece_position(self, selected_square, move_to_square):
        # this moves the piece

        selected_piece = self.square_occupied_by(selected_square)

        for piece in self.board.pieces:
            if piece.position == selected_piece.position:
                piece.position = move_to_square

    def end_game(self):
        pass

    def checkmate(self):
        pass


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


class Piece():
    def __init__(self, name, icon, color, position):
        self.name = name
        self.icon = icon
        self.color = color
        self.position = position
        
        

    def check_top(self, selected_square):
        # checks the square on top of the piece
        
        pass

    def check_bottom(self):
        pass

    def check_left(self):
        pass

    def check_right(self):
        pass

    def check_diagonal(self):
        # checks the diagonals of the piece

        pass

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Pawn",
        icon = "♟",       
        color = color,
        position = position 
        )
    
    def pawn_valid_move(self, selected_square, move_to_square):
        # checks if the inputted square is a valid move for a pawn 
        
        if self.color == "WHITE":
            if int(selected_square[1]) < int(move_to_square[1]) <= (int(selected_square[1]) + int(2)):
                return "VALID"
        else:
            if (int(selected_square[1]) - int(2)) <= int(move_to_square[1]) < int(selected_square[1]):
                return "VALID"


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Rook",
        icon = "♜",       
        color = color,
        position = position 
        )

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Knight",
        icon = "♞",       
        color = color,
        position = position 
        )

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Bishop",
        icon = "♝",       
        color = color,
        position = position 
        )

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Queen",
        icon = "♛",       
        color = color,
        position = position 
        )

class King(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "King",
        icon = "♚",       
        color = color,
        position = position 
        )
    

if __name__ == "__main__":
    game = Chess()

    game.start_game()

