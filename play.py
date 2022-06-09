from gridworld_env import GridworldEnv
from agent import QTableAgent
import numpy as np

# init agent
agent = QTableAgent()
agent.verbose = True
agent.load_q_table('q_table.npy')
agent.epsilon = 0 # tryhard enabled

print("Showing", agent.name, "with gamma =", agent.gamma, end=":\n\n")

# init environment
env = GridworldEnv()
state = env.reset()
env.render()
print()

for t in range(10):
    action = agent.get_action(state, env.get_action_space())
    next_state, reward, done = env.step(action)
    print()
    env.render()
    print(next_state, reward, done)
    print()
    state = next_state
    if done:
        print("Episode terminated.\n")
        env.reset()
        break