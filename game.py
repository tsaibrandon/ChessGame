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
        if self.turn == "WHITE":
            self.turn = "BLACK"
        else: 
            self.turn = "WHITE"

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
            
            if not self.board.is_empty_square(to_square):
                print("Square is occupied! Please select an empty square.\n")
                continue

            break
            
            # return to_square
    