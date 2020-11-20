import numpy as np
import random

HIGHT = 5
WIDTH = 5


class environment:
    def __init__(self):
        self.field = np.zeros(HIGHT * WIDTH)
        self.number_states = HIGHT * WIDTH
        self.number_actions = 4
        self.state
        self.next_state
        self.special_10_start_state = 1
        self.special_10_end_state = 21
        self.special_5_start_state = 3
        self.special_5_end_state = 13
    #########################
    ##       Actions       ##
    ##        N = 0        ##
    ## W = 4         O = 1 ##
    ##        S = 3        ##
    #########################
    def step(self, action, state):
        if state == self.special_10_start_state:
            return 10, 21
        if state == self.special_5_start_state:
            return 5, 14
        if action == 0:
            if state <= WIDTH - 1:
                return -1, state
            else:
                newState = state - WIDTH
                return 0, np.array(newState)
        elif action == 1:
            # right boarder in this case 4, 9, 14 usw
            if state + 1 % 5 == 0:
                return -1, state
            else:
                newState = state + 1
                return 0, np.array(newState)
        elif action == 2:
            if state >= WIDTH * HIGHT - WIDTH:
                return -1, state
            else:
                newState = state + WIDTH
                return 0, np.array(newState)
        elif action == 3:
            if state % WIDTH == 0:
                return -1, state
            else:
                newState = state - 1
                return 0, np.array(newState)

    def get_action(self):
        return random.randint(0, 3)

    def print_field(self):
        print(self.field)
