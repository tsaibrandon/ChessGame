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
        if self.turn == "White":
            self.turn = "Black"
        else: 
            self.turn = "White"


    # def coordinate_to_index(self, selected_square):
    #     # changes user input to array notation

    #     col = selected_square[0]
    #     col = self.board.col_labels[col]
    #     row = 8 - int(selected_square[1])
    #     return row, col
    
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


    