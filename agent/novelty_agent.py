from agent import Agent

import random
import copy

class NoveltyAgent(Agent):
    def __init__(self, place_cell):
        self.place_cell = place_cell
        self.wall_information = {}

    def choose_action(self):
        EPSILON = 0.1

        if random.random() < EPSILON:
            action = random.choice(self.get_available_actions())
        else:
            action = self.choose_action_greedy()
        return action

    def choose_action_greedy(self):
        best_actions = []
        max_novelty = 0

        max_traverse_step = 3
        for action in self.get_available_actions():
            child = copy.deepcopy(self)
            child.place_cell.move(action)
            predicted_novelty = child.traverse_maze(max_traverse_step - 1)
            if predicted_novelty > max_novelty:
                best_actions = [action]
                max_novelty = predicted_novelty
            elif predicted_novelty == max_novelty:
                best_actions.append(action)
        return random.choice(best_actions)

    def traverse_maze(self, step):
        novelty = self.place_cell.novelty
        if step > 0:
            current_coordinate = self.place_cell.coordinate_id()
            for action in self.get_available_actions():
                self.place_cell.set_coordinate_id(current_coordinate)
                self.place_cell.move(action)
                novelty += self.traverse_maze(step - 1)
        return novelty

    def get_available_actions(self):
        wall = self.wall_information.setdefault(self.place_cell.coordinate_id(), (0, 0, 0, 0))
        available_actions = []
        for action in range(0, 4):
            if (not wall[action]) and self.place_cell.validate_action(action):
                available_actions.append(action)
        return available_actions

    def set_wall(self, wall):
        self.wall_information[self.place_cell.coordinate_id()] = wall
