import gym
import numpy as np

class QLearningAgent:

    def __init__(self, env):
        # Initialize Q-learning agent parameters
        self.env = env
        self.alpha = 0.1  # Learning rate
        self.gamma = 0.9  # Discount factor
        self.epsilon = 0.1  # Exploration probability
        self.q_values = {}  # Initialize Q-values table

    def act(self, state):
        # Select action based on epsilon-greedy policy
        if np.random.rand() < self.epsilon:
            action = self.env.action_space.sample()  # Random exploration
        else:
            action = np.argmax(self.q_values[state])  # Exploit best action

        return action

    def learn(self, state, action, reward, next_state):
        # Update Q-values table using Bellman equation
        q_current = self.q_values.get((state, action), 0)
        q_prime = np.max(self.q_values.get(next_state, [0]))  # Optimal future reward
        updated_q = q_current + self.alpha * (reward + self.gamma * q_prime - q_current)
        self.q_values[(state, action)] = updated_q

    def save_model(self, filename):
        # Save Q-values table to a file
        np.save(filename, self.q_values)

    def load_model(self, filename):
        # Load Q-values table from a file
        self.q_values = np.load(filename)