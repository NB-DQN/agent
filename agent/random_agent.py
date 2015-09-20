from agent import Agent

import random

class RandomAgent(Agent):
    def __init__(self, environment):
        self.environment = environment

    def choose_action(self):
        a = random.choice(self.get_available_actions())
        return a

    def get_available_actions(self):
        wall = self.environment.wall()
        actions = []
        for a in range(0, 4):
            if wall[a] == 0:
                actions.append(a)
        return actions
