from abc import ABC, abstractmethod

class Goalie(ABC):
    def __init__(self, id, behaviour=None):
        self.id = id
        self.behaviour = behaviour

    @abstractmethod
    def run(self):
        pass

chillBot = Robot()