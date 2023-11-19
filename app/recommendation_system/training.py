import gym
import numpy as np
from qlearning_agent import QLearningAgent

env = gym.make('F1-v0')  # Replace with the appropriate environment name

agent = QLearningAgent(env)

episodes = 1000  # Number of training episodes
for episode in range(episodes):
    done = False
    state = env.reset()

    while not done:
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state

    print(f"Episode {episode+1} complete")

agent.save_model('q_learning_model.h5')