import gym
import numpy as np
from qlearning_agent import QLearningAgent

env = gym.make('F1-v0')  # Replace with the appropriate environment name

agent = QLearningAgent(env)
agent.load_model('q_learning_model.h5')

episodes = 100  # Number of evaluation episodes
for episode in range(episodes):
    done = False
    state = env.reset()

    while not done:
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        env.render()  # Render the environment if desired
        state = next_state

    print(f"Episode {episode+1} complete")
