import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

class DQNAgent:
    def __init__(self, state_size, action_size, alpha, gamma, epsilon):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.model = self._build_model()

    def _build_model(self):
        model = nn.Sequential(
            nn.Linear(self.state_size, 24),
            nn.ReLU(),
            nn.Linear(24, 24),
            nn.ReLU(),
            nn.Linear(24, self.action_size)
        )
        return model

    def choose_action(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        state = torch.FloatTensor(state).view(1, -1)
        act_values = self.model(state)
        return torch.argmax(act_values).item()

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        if len(self.memory) < batch_size:
            return

        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                next_state = torch.FloatTensor(next_state).view(1, -1)
                target = (reward + self.gamma * torch.max(self.model(next_state).detach()).item())
            state = torch.FloatTensor(state).view(1, -1)
            target_f = self.model(state)
            target_f[0][action] = target
            self.model.train()
            criterion = nn.MSELoss()
            optimizer = optim.Adam(self.model.parameters(), lr=self.alpha)
            optimizer.zero_grad()
            loss = criterion(target_f, self.model(state))
            loss.backward()
            optimizer.step()

        if self.epsilon > 0.01:
            self.epsilon *= 0.995
