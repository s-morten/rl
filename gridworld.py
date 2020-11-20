import numpy as np
import random

HIGHT = 5
WIDTH = 5


class environment:
    def __init__(self):
        self.field = np.zeros(HIGHT * WIDTH)
        self.number_states = HIGHT * WIDTH
        self.number_actions = 4
        self.state = None
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
        if state is None:
            state = self.state
        # print(f"state in thingy: {state}")
        if state == self.special_10_start_state:
            return 10, self.special_10_end_state
        if state == self.special_5_start_state:
            return 5, self.special_5_end_state
        if action == 0:
            if state <= WIDTH - 1:
                return -1, state
            else:
                newState = state - WIDTH
                self.state = newState
                return 0, np.array(newState)
        elif action == 1:
            # right boarder in this case 4, 9, 14 usw
            if (state + 1) % 5 == 0:
                return -1, state
            else:
                newState = state + 1
                self.state = newState
                return 0, np.array(newState)
        elif action == 2:
            if state >= WIDTH * HIGHT - WIDTH:
                return -1, state
            else:
                newState = state + WIDTH
                self.state = newState
                return 0, np.array(newState)
        elif action == 3:
            if state % WIDTH == 0:
                return -1, state
            else:
                newState = state - 1
                self.state = newState
                return 0, np.array(newState)

    def get_action(self):
        return random.randint(0, 3)

    def print_field(self):
        print(self.field)


env = environment()
random_policy = np.ones([env.number_states, env.number_actions]) / env.number_actions
gamma = 0.9
epsilon = 0.00001


def policy_evaluation(policy, env):
    V_old = np.zeros(env.number_states)
    while True:
        V_new = np.zeros(env.number_states)
        delta = 0
        for s in range(env.number_states):
            v = 0
            action_probs = policy[s]
            for a in range(env.number_actions):
                reward, next_state = env.step(a, s)

                v += action_probs[a] * (reward + gamma * V_old[next_state])
            delta = max(delta, abs(v - V_old[s]))
            V_new[s] = v
        V_old = V_new
        if(delta < epsilon):
            return V_old


action_prbability = np.ones([env.number_states, env.number_actions]) / env.number_actions
policy = random_policy
actions_values = np.zeros(env.number_actions)


def policy_improvement(env):
    # use V from policy evaluation
    V_old = policy_evaluation(policy, env)

    for s in range(env.number_states):
        actions = np.zeros(env.number_actions)
        # one step look ahead
        for a in range(env.number_actions):
            reward, next_state = env.step(a, s)
            actions[a] = action_prbability[s][a] * (reward + gamma * V_old[next_state])
        actions_values = actions
        best_action = np.argmax(actions_values)

        policy[s] = np.eye(env.number_actions)[best_action]
    return policy, V_old


def policy_iteration(env):
    while True:
        # stable flag for iteration
        policy_stable = True
        V_old = policy_evaluation(policy, env)

        for s in range(env.number_states):
            actions = np.zeros(env.number_actions)
            # one step look ahead
            for a in range(env.number_actions):
                reward, next_state = env.step(a, s)
                actions[a] = action_prbability[s][a] * (reward + gamma * V_old[next_state])
            actions_values = actions
            best_action = np.argmax(actions_values)
            chosen_action = np.argmax(policy[s])

            # update stable for possible finish flag
            if(best_action != chosen_action):
                policy_stable = False

            policy[s] = np.eye(env.number_actions)[best_action]

        # nothing changed, finished!
        if(policy_stable):
            return policy, V_old


def value_iteration(env):
    # start with zeros
    V = np.zeros(env.number_states)
    policy = np.zeros([env.number_states, env.number_actions])

    while True:
        delta = 0
        for s in range(env.number_states):
            actions_values = np.zeros(env.number_actions)
            # one step look ahead
            for a in range(env.number_actions):
                reward, next_state = env.step(a, s)
                v = action_prbability[s][a] * (reward + gamma * V[next_state])
                actions_values[a] = v

            best_action_value = max(actions_values)
            delta = max(delta, abs(best_action_value - V[s]))

            V[s] = best_action_value
            best_action = np.argmax(actions_values)
            policy[s] = np.eye(env.number_actions)[best_action]

        # nothing / not enough has changed, finsish
        if(delta < epsilon):
            break

    return policy, V


print("######  Policy Evaluation ######")
V = policy_evaluation(random_policy, env)
print("V:")
print(V)
print("######  Policy Improvement ######")
policy, V = policy_improvement(env)
print("policy:")
print(np.reshape(np.argmax(policy, axis=1), (5, 5)))
print("V:")
print(V)
print("######  Policy Iteration ######")
policy, V = policy_iteration(env)
print("policy:")
print(np.reshape(np.argmax(policy, axis=1), (5, 5)))
print("V:")
print(V)
print("######  Value Iteration ######")
policy, V = value_iteration(env)
print("policy:")
print(np.reshape(np.argmax(policy, axis=1), (5, 5)))
print("V:")
print(V)
