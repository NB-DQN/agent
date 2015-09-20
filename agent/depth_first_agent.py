from agent import Agent

import random

class DepthFirstAgent(Agent):
    def __init__(self, environment):
        self.environment = environment
        self.stack = {}

    def choose_action(self):
        s = self.environment.coordinate_id()
        non_wall = self.stack.setdefault(s, self.non_wall(s))
        actions = []
        for a in range(0, 4):
            if non_wall[a] == 1:
                actions.append(a)

        if len(actions) > 0:
            action = random.choice(actions)
            self.stack[s][action] = 0
            self.environment.move(action)

            if   action == 0:
                a = 1
            elif action == 1:
                a = 0
            elif action == 2:
                a = 3
            elif action == 3:
                a = 2
            s = self.environment.coordinate_id()
            self.stack.setdefault(s, self.non_wall(s))
            self.stack[s][a] = 10
        else:
            self.environment.move(non_wall.index(10))

    def non_wall(self, s):
        wall = self.environment.wall(s)
        return [0 if wall[i] else 1 for i in range(0, 4)]
