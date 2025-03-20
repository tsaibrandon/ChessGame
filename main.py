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

        while True:
            first_input = input("Select a piece you want to move (e.g. 'e2'): ")
            if not valid_input(first_input):
                continue

            second_input = input("Select a square to move to (e.g. 'e4'): ")
            if not valid_input(second_input):
                continue

            break
        
        game.player_turn()

if __name__ == "__main__":
    main()

