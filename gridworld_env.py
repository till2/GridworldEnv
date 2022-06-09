# Toy grid environment for Reinforcement Learning

class GridworldEnv():
    def __init__(self):
        self.state = (0,0) # x,y
        self.action_space = [(0,1), (0,-1), (1,0), (-1,0)] # up down right left
        self.reward_space = [-1, 0, 1]
        self.done = False
        self.reward = 0
    
    def step(self, action):
        """
        Takes an action and returns the next state, reward, and done
        """
        if self.done:
            return self.state, self.reward, self.done
        state_x = self.state[0]
        state_y = self.state[1]
        if self.state[0] + action[0] in [0,1,2]:
            state_x = self.state[0] + action[0]
        if self.state[1] + action[1] in [0,1,2]:
            state_y = self.state[1] + action[1]
        self.state = (state_x, state_y)

        if self.state in [(1,0), (2,0)]:
            self.done = True

        if self.state == (1,0):
            self.reward = -1
        elif self.state == (2,0):
            self.reward = 1
        else:
            self.reward = 0
        return self.state, self.reward, self.done
    
    def get_action_space(self):
        """
        Returns the valid action space of the environment given the current state
        """
        action_space = []
        for action in self.action_space:
            if self.state[0] + action[0] in [0,1,2] and self.state[1] + action[1] in [0,1,2]:
                action_space.append(action)
        return action_space
    
    def reset(self):
        """
        Resets the environment to its initial state
        """
        self.state = (0,0)
        self.done = False
        self.reward = 0
        return self.state
    
    def render(self):
        """
        Prints a text representation of the current position of the agent (state).
        """
        for j in range(3):
            for i in range(3):
                if self.state == (i,2-j):
                    print('a', end='')
                elif (1,0) == (i,2-j):
                    print('-', end='')
                elif (2,0) == (i,2-j):
                    print('+', end='')
                else:
                    print('*', end='')
            print()