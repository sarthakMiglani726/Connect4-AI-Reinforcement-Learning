class ConnectFour:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_turn = 'X'  # X will start by default

    def print_board(self):
        print(" 1 2 3 4 5 6 7")
        for row in self.board:
            print('|' + '|'.join(row) + '|')

    def is_valid_move(self, column):
        if 0 <= column < 7 and self.board[0][column] == ' ':
            return True
        return False

    def make_move(self, column):
        """Handles making a move and toggling turns."""
        if self.is_valid_move(column):
            for i in range(5, -1, -1):
                if self.board[i][column] == ' ':
                    self.board[i][column] = self.current_turn
                    break
            
            # Toggle turn after valid move
            self.toggle_turn()
            return True
        return False


    def check_winner(self):
        # Horizontal, vertical, and diagonal checks
        for row in range(6):
            for col in range(7):
                if self.board[row][col] != ' ':
                    # Check horizontal
                    if col <= 3 and all(self.board[row][col + i] == self.board[row][col] for i in range(4)):
                        return self.board[row][col]
                    # Check vertical
                    if row <= 2 and all(self.board[row + i][col] == self.board[row][col] for i in range(4)):
                        return self.board[row][col]
                    # Check diagonal /
                    if row <= 2 and col <= 3 and all(self.board[row + i][col + i] == self.board[row][col] for i in range(4)):
                        return self.board[row][col]
                    # Check diagonal \
                    if row >= 3 and col <= 3 and all(self.board[row - i][col + i] == self.board[row][col] for i in range(4)):
                        return self.board[row][col]
        return None

    def is_draw(self):
        if all(self.board[0][col] != ' ' for col in range(7)):
            return True
        return False
    
    def is_over(self):
        return self.check_winner() is not None or self.is_draw()

    def reset_board(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_turn = 'X'  # Reset to default or switch according to your game rules

    def toggle_turn(self):
        self.current_turn = 'O' if self.current_turn == 'X' else 'X'

    def state_to_tuple(self):
        # Convert the game board to numerical values: 'X' -> 1, 'O' -> -1, ' ' -> 0
        return tuple(tuple(1 if cell == 'X' else -1 if cell == 'O' else 0 for cell in row) for row in self.board)
    