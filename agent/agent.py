from abc import ABCMeta, abstractmethod

class Agent(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def choose_action(self):
        pass
