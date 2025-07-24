from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, id):
        self.id = id
        self.behaviour = self.assign_behaviour()

    @abstractmethod
    def active(self):
        pass

    @abstractmethod
    def assign_behaviour(self):
        pass

    @abstractmethod
    def idle(self):
        pass