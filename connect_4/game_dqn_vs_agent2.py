from connect_four import ConnectFour
from connect_four_gui import ConnectFourGUI
from agent_dqn import DQNAgent
from agent_q_learning import QLearningAgent
from agent_sarsa import SARSAgent
from config import Config
import matplotlib.pyplot as plt
import tkinter as tk

def simulate_game(agent1, agent2, display=False):
    game = None
    root = None
    gui = None

    if display:
        root = tk.Tk()  # Create a Tkinter window
        gui = ConnectFourGUI(root)  # Initialize the GUI
        game = gui.game  # Use the GUI's game instance
        root.update()  # Update the GUI to display initial state
    else:
        game = ConnectFour()  # Initialize the game if no display

    agents = {'X': agent1, 'O': agent2}  # Map agents to symbols

    while not game.is_over():
        current_turn = game.current_turn  # Get the current turn symbol
        current_state = game.state_to_tuple()  # Use the correct method to get the game state as a sequence
        action = agents[current_turn].choose_action(current_state)  # Agent chooses an action based on the state
        game.make_move(action)  # Make the move

        if display:
            gui.update_game_state()  # Update the GUI state
            root.update_idletasks()  # Refresh the GUI window
            root.update()  # Process events

    if display:
        root.after(500, root.destroy)  # Schedule the window to close after 500 ms
        root.mainloop()  # Start the Tkinter event loop to keep the window open

    return game.check_winner()  # Return the winner symbol, or None if draw



def main():
    # Initialize DQN and SARSA agents
    dqn_agent = DQNAgent(state_size=Config.STATE_SIZE, action_size=Config.ACTION_SPACE, alpha=Config.ALPHA, gamma=Config.GAMMA, epsilon=Config.EPSILON)
    q_agent = QLearningAgent(alpha=Config.ALPHA, gamma=Config.GAMMA, epsilon=Config.EPSILON)
    sarsa_agent = SARSAgent(alpha=Config.ALPHA, gamma=Config.GAMMA, epsilon=Config.EPSILON)
    
    """DQN vs Q-learning"""
    # Displaying and playing the first 10 games with GUI for DQN vs. Q-Learning
    print("Displaying the first 10 games (DQN vs. Q-Learning):")
    for i in range(10):
        winner = simulate_game(dqn_agent, q_agent, display=True)
        winner_text = "Draw" if winner is None else "DQN Agent" if winner == 'X' else "Q-Learning Agent"
        print(f"Game {i+1} Winner: {winner_text}")

    # Simulate all remaining games from Config.NUM_EPISODES without GUI
    dqn_wins = 0
    q_wins = 0
    num_games = Config.NUM_EPISODES - 10

    for _ in range(num_games):
        winner = simulate_game(dqn_agent, q_agent)
        if winner == 'X':
            dqn_wins += 1
        elif winner == 'O':
            q_wins += 1
    
    # Displaying the results
    draws = num_games - dqn_wins - q_wins

    print(f"\nResults of {num_games} games:")
    print(f"DQN Agent wins: {dqn_wins}")
    print(f"Q-learning Agent wins: {q_wins}")
    print(f"Draws: {draws}")

    # Plotting the results
    labels = ['DQN Wins', 'Q-learning Wins', 'Draws']
    counts = [dqn_wins, q_wins, draws]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, counts, color=['blue', 'green', 'gray'])
    plt.xlabel('Results')
    plt.ylabel('Counts')
    plt.title(f'DQN vs. Q-learning in {num_games} Connect Four Games')

    # Adding data labels above each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=10)
    plt.show()

    """DQN vs SARSA"""
    # Displaying and playing the first 10 games with GUI for DQN vs. SARSA
    print("Displaying the first 10 games (DQN vs. SARSA):")
    for i in range(10):
        winner = simulate_game(dqn_agent, sarsa_agent, display=True)
        winner_text = "Draw" if winner is None else "DQN Agent" if winner == 'X' else "SARSA Agent"
        print(f"Game {i+1} Winner: {winner_text}")

    # Simulate all remaining games from Config.NUM_EPISODES without GUI
    dqn_wins = 0
    sarsa_wins = 0
    num_games = Config.NUM_EPISODES - 10
    
    for _ in range(num_games):
        winner = simulate_game(dqn_agent, sarsa_agent)
        if winner == 'X':
            dqn_wins += 1
        elif winner == 'O':
            sarsa_wins += 1

    # Displaying the results
    draws = num_games - dqn_wins - sarsa_wins


    print(f"\nResults of {num_games} games (DQN vs. SARSA):")
    print(f"DQN Agent wins: {dqn_wins}")
    print(f"SARSA Agent wins: {sarsa_wins}")
    print(f"Draws: {draws}")

    # Plotting the results
    labels = ['DQN Wins', 'SARSA Wins', 'Draws']
    counts = [dqn_wins, sarsa_wins, draws]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, counts, color=['red', 'green', 'gray'])
    plt.xlabel('Outcome')
    plt.ylabel('Number of Games')
    plt.title(f'Results of DQN vs. SARSA in {num_games} Connect Four Games')

    # Adding data labels above each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom', fontsize=10)
    plt.show()

if __name__ == "__main__":
    main()
