from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, id):
        self.id = id
        self.behaviour = self.assign_behaviour()

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def assign_behaviour(self):
        pass