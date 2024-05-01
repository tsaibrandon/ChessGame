player_1 = 1
player_2 = 2
whos_turn = 1 

class Chess:
    """
        This engine of the game. Where all the basic rules are kept to make sure the game runs properly.
    """
    def __init__(self):
        self.board = Board()

    def game_engine(self):
        # if it is not checkmate then the game continues
        # if checkmate detected then game ends

        return True

    
    def start_game(self):
        # initializes players, board, and pieces

        self.board.create_board()

        while self.game_engine():
            self.player_turn()
        

    def player_turn(self):
        global whos_turn
        self.check_turn()
        if self.check_turn() == player_1:
            print("It's WHITE's turn!")
            white_select_piece = input("Which piece would you like to move? ")
            print(white_select_piece)
            whos_turn += 1 
            print(whos_turn)
        else:
            print("It's BLACK's turn!")
            black_select_piece = input("Which piece would you like to move? ")
            print(black_select_piece)
            whos_turn -= 1
            print(whos_turn)

    def check_turn(self):
        if whos_turn == 1:
            return player_1
        else:
            return player_2

    def end_game(self):
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
    
    def create_board(self):
        for row in self.board:
            print(" ".join(row))
    
    def update_board(self):
        pass


class Piece():
    def __init__(self, color, id):
        self.color = color
        self.id = id

    def check_color(self):
        pass 
    
    def check_type(self):
        pass

class Pawn(Piece):
#    ♟     
    pass                 

class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass
    

if __name__ == "__main__":
    game = Chess()

    game.start_game()
