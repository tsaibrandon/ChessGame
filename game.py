from board import Board
from pieces import Pawn, Rook, Knight, Bishop, Queen, King

class Chess:
    """
        This engine of the game. Where all the basic rules are kept to make sure the game runs properly.
    """
    def __init__(self):
        self.board = Board()
        self.turn = "White"
        

    def start_game(self):
        # initializes players, board, and pieces
        self.board.initialize_pieces()
        self.board.create_board()

    def player_turn(self):
        # gets players input for pieces to move where 
        
        # selected_square = input(
        #     f"It's {self.check_turn()}'s turn!\n"
        #     "Enter the square of the piece would you like to move: "
        # )
        
        # self.is_valid_piece(selected_square)

        # move_to_square = input(
        #     "Enter the square you would like to move your piece to: "
        # )

        # self.move_piece(selected_square, move_to_square)

        if self.turn == "White":
            self.turn = "Black"
        else: 
            self.turn = "White"
        
        # Switch turns after a move
        # if self.turn == 1:
        #     self.turn = 2
        # else:
        #     self.turn = 1

    # def check_turn(self):
    #     # returns who's turn it is

    #     if self.turn == 1:
    #         return "WHITE"
    #     else:
    #         return "BLACK"

    def coordinate_to_index(self, selected_square):
        # changes user input to array notation

        col = selected_square[0]
        col = self.board.col_labels[col]
        row = 8 - int(selected_square[1])
        return row, col
    
    # def end_game(self):
    #     pass

    def checkmate(self):
        return False

    def game_engine(self):
        if self.checkmate() == False:
            return True
        else:
            print(f"Checkmate! {self.turn} wins!")
            return False


    def is_valid_piece(self, selected_square):
        # Placeholder for validating piece selection
        pass
        
    def move_piece(self, selected_square, move_to_square):
        # Placeholder for moving pieces
        pass