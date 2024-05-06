import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import connect_four
import agent_sarsa
import agent_dqn
import agent_q_learning
from config import Config

def reset_game(display_message=None):
    if display_message:
        messagebox.showinfo("Game Over", display_message)
    # Reset the game board to start state with 'X' (you) starting
    game.reset_board()
    update_board()

def drop_piece(col):
    if game.is_valid_move(col):
        # Make the move on the board
        game.make_move(col)
        update_board()
        check_game_status()
        if not game.is_over():
            ai_move()
        check_game_status()

def ai_move():
    # AI chooses an action based on the current state of the board
    col = game.ai_agent.choose_action(game.state_to_tuple())
    if game.is_valid_move(col):
        game.make_move(col)
        update_board()
    check_game_status()

def check_game_status():
    if game.is_over():
        winner = game.check_winner()
        if winner:
            reset_game(f"Winner is: {winner}")
        else:
            reset_game("It's a draw!")

def update_board():
    for row in range(6):
        for col in range(7):
            buttons[row][col].config(text=game.board[row][col])

def model_selected(event):
    model_name = model_var.get()
    if model_name == "SARSA":
        game.ai_agent = agent_sarsa.SARSAgent(Config.ALPHA, Config.GAMMA, Config.EPSILON)
    elif model_name == "DQN":
        game.ai_agent = agent_dqn.DQNAgent(Config.STATE_SIZE, Config.ACTION_SPACE, Config.ALPHA, Config.GAMMA, Config.EPSILON)
    elif model_name == "Q-Learning":
        game.ai_agent = agent_q_learning.QLearningAgent(Config.ALPHA, Config.GAMMA, Config.EPSILON)

app = tk.Tk()
app.title("Connect 4")

model_var = tk.StringVar()
model_dropdown = ttk.Combobox(app, textvariable=model_var, values=["SARSA", "DQN", "Q-Learning"])
model_dropdown.grid(row=0, column=0, columnspan=3)
model_dropdown.bind("<<ComboboxSelected>>", model_selected)

reset_button = tk.Button(app, text="Reset", command=lambda: reset_game())
reset_button.grid(row=0, column=4, columnspan=3)

buttons = []
game = connect_four.ConnectFour()

for row in range(6):
    button_row = []
    for col in range(7):
        button = tk.Button(app, text='', width=10, height=3, command=lambda c=col: drop_piece(c))
        button.grid(row=row+1, column=col)
        button_row.append(button)
    buttons.append(button_row)

app.mainloop()
