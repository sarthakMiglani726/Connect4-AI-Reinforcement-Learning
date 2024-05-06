from connect_four import ConnectFour

def test_connect_four():
    game = ConnectFour()
    game.print_board()

    moves = [0, 1, 1, 2, 3, 2, 2, 3, 4, 3, 3]  # Resulting in a win for 'X'
    for move in moves:
        if game.make_move(move):
            print(f"Successfully placed on column {move + 1}")
            game.print_board()

            # Check for winner or draw
            winner = game.check_winner()
            if winner:
                print(f"Winner: {winner}")
                break
            elif game.is_draw():
                print("It's a draw!")
                break

        else:
            print(f"Failed to place on column {move + 1}")
            
        # The `toggle_turn` function is already called in `make_move`
        # No need to call it explicitly here.

    if not game.check_winner() and not game.is_draw():
        print("No winner yet.")

# Run the test
test_connect_four()
