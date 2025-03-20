from game import Chess

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
    game.start_game()
    
    # Game loop
    while game.game_engine():
        print(f"It's {game.turn}'s turn")

        selected_piece = False

        while not selected_piece:
            #implement a way so that the board stays in view even if there is too much text appearing while validating a piece move
            first_input = input("Enter the square of your piece (e.g. 'e2'): ")
            if valid_input(first_input):
                piece_color = game.board.get_piece_color(game.board.get_piece_at(first_input)) 

                if piece_color == None:
                    print("There is no piece there! Please select one of your pieces.\n")
                    continue
                elif piece_color != game.turn:
                    print("This is not your piece. Please select one of your pieces.\n")
                    continue
                else:
                    selected_piece = True
            else:
                continue

        while selected_piece:
            second_input = input("Select a square to move to (e.g. 'e4'): ")
            if valid_input(second_input):
                if game.board.is_empty_square(second_input) == False:
                    print("Square is occupied! Please select an empty square.\n")
                    continue
            break
        
        game.player_turn()

if __name__ == "__main__":
    main()

