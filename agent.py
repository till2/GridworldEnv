# Q Table Agent
import numpy as np
import random

action_to_text = {
    (0,1): 'up',
    (0,-1): 'down',
    (1,0): 'right',
    (-1,0): 'left'
}

class QTableAgent():
    def __init__(self):
        self.name = 'jeff'
        self.q_table = {}
        self.epsilon = 0.3
        self.gamma = 0.9
        self.lr = 0.1
        self.verbose = False # for debugging

    def get_action(self, state, action_space):
        # random action
        if random.random() < self.epsilon:
            action = random.choice(action_space)
            if self.verbose:
                print("choosing random action", action, "in state", state)
        # greedy action
        else:
            if state not in self.q_table.keys():
                self.q_table[state] = {}
                action = random.choice(action_space)
            else:
                if self.verbose:
                    print("my choices are:")
                max_action = None
                max_value = -np.inf
                for key, value in zip(self.q_table[state].keys(), self.q_table[state].values()):
                    if self.verbose:
                        print(action_to_text[key], "is worth", round(value, 2))
                    if value > max_value:
                        max_value = value
                        max_action = key
                action = max_action
            if self.verbose:
                print("choosing greedy action", action_to_text[action], "in state", state)
        return action

    def update(self, state, action, reward, next_state, done):
        if self.verbose:
            print("updating with reward =",reward, "done =",done)
        if state not in self.q_table.keys():
            self.q_table[state] = {}
        if not done and next_state not in self.q_table.keys():
            self.q_table[next_state] = {}
            self.q_table[next_state][action] = 0
        if action not in self.q_table[state].keys():
            self.q_table[state][action] = 0
        
        if done:
            if self.verbose:
                print("updating step into terminal state")
                print("value before update:" , self.q_table[state][action], end=" ")
            old_q_value = self.q_table[state][action]
            target_q_value = reward # no future reward
            self.q_table[state][action] = (1-self.lr) * old_q_value + self.lr * target_q_value
            if self.verbose:
                print("and after:" , self.q_table[state][action])
                print("old, target:", old_q_value, target_q_value)
                print()

        else:
            max_action = None
            max_next_value = -np.inf
            for value in self.q_table[next_state].values():
                if value > max_next_value:
                    max_next_value = value
            if max_next_value == -np.inf:
                max_next_value = 0
            if self.verbose:
                print("value before update:" , self.q_table[state][action], end=" ")
            old_q_value = self.q_table[state][action]
            target_q_value = reward + self.gamma * max_next_value
            self.q_table[state][action] = (1-self.lr) * old_q_value + self.lr * target_q_value
            if self.verbose:
                print("and after:" , self.q_table[state][action])
                print("old, target:", old_q_value, target_q_value)
                print("max next value:", max_next_value)
                print()
    
    def save_q_table(self, filename):
        np.save(filename, self.q_table)
    
    def load_q_table(self, filename):
        self.q_table = np.load(filename, allow_pickle=True).item()