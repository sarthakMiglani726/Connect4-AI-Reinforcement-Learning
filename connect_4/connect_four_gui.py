import tkinter as tk
from connect_four import ConnectFour

class ConnectFourGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect Four")
        
        # Initialize game logic
        self.game = ConnectFour()

        # Create a 6x7 grid of buttons
        self.buttons = []
        for i in range(6):
            row = []
            for j in range(7):
                btn = tk.Button(self.master, width=10, height=4, command=lambda col=j: self.make_move(col))
                btn.grid(row=i, column=j)
                row.append(btn)
            self.buttons.append(row)
        
        # Create labels to show the current turn or winner
        self.turn_label = tk.Label(self.master, text=f"Turn: {self.game.current_turn}")
        self.turn_label.grid(row=6, columnspan=7)

    def make_move(self, column):
        """Handles the logic for making a move and toggling turns."""
        if self.game.make_move(column):
            self.update_game_state()  # Update the GUI board after a move
            winner = self.game.check_winner()

            if winner:
                self.turn_label.config(text=f"Winner: {winner}")
                self.disable_buttons()
            elif self.game.is_draw():
                self.turn_label.config(text="It's a draw!")
                self.disable_buttons()
            else:
                # Refresh turn label after toggling turn
                self.turn_label.config(text=f"Turn: {self.game.current_turn}")

    def update_game_state(self):
        """Updates the GUI to reflect the game board."""
        for i in range(6):
            for j in range(7):
                self.buttons[i][j].config(text=self.game.board[i][j])

    def disable_buttons(self):
        """Disables all buttons once the game is over."""
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

def main():
    root = tk.Tk()
    app = ConnectFourGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()