from game import Chess
from board import Board

def valid_input(input):
    if len(input) == 2:
        if input[0].isalpha() and input[1].isdigit():
            return True
        else:
            print("Your input is invalid! Please try again.\n")
            return False
    else:
        print("Your input is invalid! Please try again.\n")
        return False

def main():
    game = Chess()
    board = Board()
    game.start_game()
    
    # Game loop
    while game.game_engine():
        print(f"It's {game.turn}'s turn")

        while True:
            first_input = input("Enter the square of your piece (e.g. 'e2'): ")
            if not valid_input(first_input):
                continue
            else:
                piece_color = board.get_piece_color(board.get_piece_at(first_input))
                print(piece_color)

                if piece_color == None:
                    print("There is no piece there! Please select one of your pieces.")
                    continue
                elif piece_color != game.turn:
                    print("This is not your piece. Please select one of your pieces.")
                    continue

            second_input = input("Select a square to move to (e.g. 'e4'): ")
            if not valid_input(second_input):
                continue

            break
        
        game.player_turn()

if __name__ == "__main__":
    main()

