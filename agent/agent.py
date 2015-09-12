from abc import ABCMeta, abstractmethod

class Agent(object):
    __metaclass__ = ABCMeta

    def __init__(self, place_cell):
        self.place_cell = place_cell

    @abstractmethod
    def choose_action(self):
        pass
