from game import Chess

def main():
    game = Chess()
    game.start_game()
    
    # Game loop
    while game.game_engine():
        print(f"It's {game.turn}'s turn")

        game.from_square = game.valid_piece()
        game.to_square = game.valid_destination(game.from_square)
        
        game.player_turn()

if __name__ == "__main__":
    main()

