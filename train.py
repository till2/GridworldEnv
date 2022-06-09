from gridworld_env import GridworldEnv
from agent import QTableAgent
import numpy as np

# init environment
env = GridworldEnv()
state = env.reset()

# init agent
agent = QTableAgent()
print(agent.name)

reward_history = []
acc_rewards = 0

for epoch in range(1000000):
    acc_rewards = 0
    for t in range(10):
        action = agent.get_action(state, env.get_action_space())
        next_state, reward, done = env.step(action)
        agent.update(state, action, reward, next_state, done)
        state = next_state
        acc_rewards += reward
        if done:
            # print("Episode terminated.\n")
            env.reset()
            break
    if agent.epsilon > 0.05:
        agent.epsilon *= 0.999
    reward_history.append(acc_rewards)

print(reward_history)
for x in agent.q_table.keys():
    print("state ", x, "->", agent.q_table[x])

agent.save_q_table("q_table.npy")