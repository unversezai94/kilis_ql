import numpy as np

from sumo_rl.exploration.epsilon_greedy import EpsilonGreedy


class Agent:

    def __init__(self, starting_state, state_space, action_space, learning_rate=0.5, discount_factor=0.95, exploration_strategy=EpsilonGreedy()):
        self.state = starting_state
        self.state_space = state_space
        self.action_space = action_space
        self.action = None
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table = {self.state: [0 for _ in range(action_space.n)]}
        self.exploration = exploration_strategy
        self.acc_reward = 0

    # epsilon kontrolü
    def act(self):
        self.action = self.exploration.choose(self.q_table, self.state, self.action_space)
        return self.action

    def learn(self, next_state, reward, done=False):
        if next_state not in self.q_table:
            self.q_table[next_state] = [0 for _ in range(self.action_space.n)]

        s = self.state
        s1 = next_state
        a = self.action
        # bellman denklemi
        self.q_table[s][a] = self.q_table[s][a] + self.learning_rate*(reward + self.discount_factor*max(self.q_table[s1]) - self.q_table[s][a])
        self.state = s1
        self.acc_reward += reward
