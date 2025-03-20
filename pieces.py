class Piece():
    def __init__(self, name, icon, color, position):
        self.name = name
        self.icon = icon
        self.color = color
        self.position = position

    def is_valid_piece(self, selected_square):
        # checks to see if that is a piece that the player can move

        selected_piece = self.square_occupied_by(selected_square)

        if self.check_turn() == "WHITE":
            if selected_piece != "EMPTY" and selected_piece.color == "WHITE":
                print("ok")
                self.turn += 1
                return "VALID"
            elif selected_piece != "EMPTY" and selected_piece.color == "BLACK":
                print("Not valid piece")
                self.player_turn()
                return "NOT VALID"
            else:
                print("There is no piece there! Try again.")
                self.player_turn()
                return "NOT VALID"
        else:
            if selected_piece != "EMPTY" and selected_piece.color == "BLACK":
                print("ok")
                self.turn -= 1
                return "VALID"
            elif selected_piece != "EMPTY" and selected_piece.color == "WHITE":
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

        row, col = self.coordinate_to_index(selected_square)

        if self.board.board[row][col] != "-":
            for piece in self.board.pieces:
                if piece.position == selected_square:
                    return piece
        else:
            return "EMPTY"

    def move_piece(self, selected_square, move_to_square):
        # moves the selected piece

        if self.is_valid_move(selected_square, move_to_square) == "VALID":
            self.update_piece_position(selected_square, move_to_square)
            self.board.update_board()
        else:
            print("Invalid square! Please select another.")

    def is_valid_move(self, selected_square, move_to_square):
        # based on what piece is selected check to see if the piece can be moved to said square

        selected_piece = self.square_occupied_by(selected_square)
        row, col = self.coordinate_to_index(selected_square)

        if selected_piece.name == "Pawn":
            if self.is_pawn_blocked(selected_square) != "BLOCKED":
                print("not occupied")
                if selected_piece.pawn_valid_move(selected_square, move_to_square) == "VALID":
                    return "VALID"
            else:
                print("The pawn is blocked!")
                return "INVALID"
        elif selected_piece.name == "Rook":
            pass
        elif selected_piece.name == "Knight":
            pass
        elif selected_piece.name == "Bishop":
            pass
        elif selected_piece.name == "Queen":
            pass
        else:
            pass

    def check_top(self, selected_square):
        # checks the square on top of the piece
        
        top_square_coordinate = selected_square[0] + str(int(selected_square[1]) + 1)
        
        return top_square_coordinate

    def check_bottom(self, selected_square):
        # checks square below the piece 

        bottom_square_coordinate = selected_square[0] + str(int(selected_square[1]) - 1)
        
        return bottom_square_coordinate

    def check_left(self, selected_square):
        # checks square to the left of the piece

        col = selected_square[0]
        col = (int(self.board.col_labels[col]) - 1)
        col = self.board.col_labels[col]
        left_square_coordinate = col + selected_square[1]

        return left_square_coordinate        

    def check_right(self, selected_square):
        # checks the square to the right of the piece

        col = selected_square[0]
        col = (int(self.board.col_labels[col]) + 1)
        col = self.board.col_labels[col]
        right_square_coordinate = col + selected_square[1]

        return right_square_coordinate

    def check_top_left(self, selected_square):
        # checks the top left square of the selected piece

        left_square_coordinate = self.check_left(selected_square)
        top_left_coordinate = left_square_coordinate[0] + str(int(left_square_coordinate[1] + 1))

        return top_left_coordinate
    
    def check_top_right(self, selected_square):
        # checks top right square of selected piece

        right_square_coordinate = self.check_right(selected_square)
        top_right_coordinate = right_square_coordinate[0] + str(int(right_square_coordinate[1] + 1))

        return top_right_coordinate
    
    def check_bottom_left(self, selected_square):
        # checks bottom left square of selected piece

        left_square_coordinate = self.check_left(selected_square)
        bottom_left_coordinate = left_square_coordinate[0] + str(int(left_square_coordinate[1] - 1))

        return bottom_left_coordinate
    
    def check_bottom_right(self, selected_square):
        # checks bottom right square of selected piece

        right_square_coordinate = self.check_right(selected_square)
        bottom_right_coordinate = right_square_coordinate[0] + str(int(right_square_coordinate[1] - 1))

        return bottom_right_coordinate

    def is_pawn_blocked(self, selected_square):
        # checks if the selected pawn is blocked

        selected_piece = self.square_occupied_by(selected_square)
        
        top_square_coordinate = self.check_top(selected_square)
        top_square_piece = self.square_occupied_by(top_square_coordinate)
        bottom_square_coordinate = self.check_bottom(selected_square)
        bottom_square_piece = self.square_occupied_by(bottom_square_coordinate)
        
        if selected_piece.color == "WHITE":
            if top_square_piece != "EMPTY":
                return "BLOCKED"
        else:
            if bottom_square_piece != "EMPTY":
                return "BLOCKED"

    def update_piece_position(self, selected_square, move_to_square):
        # this moves the piece

        selected_piece = self.square_occupied_by(selected_square)

        for piece in self.board.pieces:
            if piece.position == selected_piece.position:
                piece.position = move_to_square
        
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
            if selected_square[1] == "2":
                if int(selected_square[1]) < int(move_to_square[1]) <= (int(selected_square[1]) + 2):
                    return "VALID"
            elif selected_square[1] != "2":
                if int(selected_square[1]) < int(move_to_square[1]) <= (int(selected_square[1]) + 1):
                    return "VALID"
            else:
                return "INVALID"
        else:
            if selected_square[1] == "7":
                if (int(selected_square[1]) - 2) <= int(move_to_square[1]) < int(selected_square[1]):
                    return "VALID"
            elif selected_square[1] != "7":
                if (int(selected_square[1]) - 1) <= int(move_to_square[1]) < int(selected_square[1]):
                    return "VALID"
            else:
                return "INVALID"


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