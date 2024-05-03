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
        # check player's turn 
        # moves their selected piece if it is a valid move

        if self.check_turn() == "White":
            white_select_piece = input(
                "\nIt's WHITE's turn!\n"
                "Which piece would you like to move? "
                )
            print(white_select_piece)
            self.board.update_board()
        else:
            black_select_piece = input(
                "\nIt's BLACK's turn!\n"
                "Which piece would you like to move? "
                )
            print(black_select_piece)
            self.board.update_board()

    def check_turn(self):
        # returns who's turn it is

        if self.turn == 1:
            self.turn += 1
            return "White"
        else:
            self.turn -=1
            return "Black"

    def check_user_input(self):
        # coordinate input read column then row
        pass

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

    def create_board(self):
        # prints out board in start state

        for row in self.board:
            print(" ".join(row))


    def update_board(self):
        pass


class Piece():
    def __init__(self, name, icon, color, position):
        self.name = name
        self.icon = icon
        self.color = color
        self.position = position

    def initial_position(self):
        # this should set the starting position based on the the cordinates that are given in the initialize function
        
        # coordinate = self.position
        # col_cord, row_cord = coordinate[0], coordinate[1]
        # col_cord = col_labels[col_cord]
        # row_cord = col_labels[row_cord]
        # col_cord, row_cord = row_cord, col_cord

        pass
        
    def check_color(self):
        pass 
    
    def check_type(self):
        pass

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(
        name = "Pawn",
        icon = "♟",       
        color = color,
        position = position 
        )


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

