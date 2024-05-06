class Config:
    # Hyperparameters
    ALPHA = 0.9  # Learning rate
    GAMMA = 0.1  # Discount factor
    EPSILON = 0.2  # Exploration rate

    # Training settings
    NUM_EPISODES = 10010  # Number of episodes for training
    STATE_SIZE = 42
    ACTION_SPACE = 7