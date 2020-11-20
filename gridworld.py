import numpy as np
import random

class environment:
    def __init__(self):
        self.field = [[0] * 5 for x in range(5)]
        self.field = np.array(self.field)

    def step(self, action, state):
        if (state == np.array([0, 1])).all():
            return 10, np.array([4, 1])
        if (state == np.array([0, 4])).all():
            return 5, np.array([2, 4])
        if action == 0:
            if state[0] == 0:
                return -1, state
            else:
                newState = [state[0] - 1, state[1]]
                return 0, np.array(newState)
        elif action == 1:
            if state[1] == 4:
                return -1, state
            else:
                newState = [state[0], state[1] + 1]
                return 0, np.array(newState)
        elif action == 2:
            if state[0] == 4:
                return -1, state
            else:
                newState = [state[0] + 1, state[1]]
                return 0, np.array(newState)
        elif action == 3:
            if state[1] == 0:
                return -1, state
            else:
                newState = [state[0], state[1] - 1]
                return 0, np.array(newState)

    def get_action(self):
        return random.randint(0,3)

    def update_value(self, state, value):
        self.field[state[0]][state[1]] = value

    def get_value(self, state):
        return self.field[state[0]][state[1]]

    def print_field(self):
        print(self.field)
