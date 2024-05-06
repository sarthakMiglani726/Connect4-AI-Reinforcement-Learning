import random

class SARSAgent:
    def __init__(self, alpha, gamma, epsilon, action_space=7):
        self.q_table = {}
        self.alpha = alpha 
        self.gamma = gamma  
        self.epsilon = epsilon 
        self.action_space = action_space 

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_space - 1)
        else:
            return self.get_best_action(state)

    def get_best_action(self, state):
        q_values = [self.q_table.get((state, a), 0) for a in range(self.action_space)]
        max_q = max(q_values)
        actions_with_max_q = [a for a, q in enumerate(q_values) if q == max_q]
        return random.choice(actions_with_max_q)

    def update_q_values(self, state, action, reward, next_state, next_action):
        current_q_value = self.q_table.get((state, action), 0)
        next_q_value = self.q_table.get((next_state, next_action), 0)
        new_q_value = current_q_value + self.alpha * (reward + self.gamma * next_q_value - current_q_value)
        self.q_table[(state, action)] = new_q_value

    def state_to_tuple(self, state):
        return tuple(tuple(row) for row in state)
