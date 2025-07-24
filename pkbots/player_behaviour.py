from .robot import Robot

class Player(Robot):
    def __init__(self, id):
        super().__init__(id)
        super().assign_behaviour()

    def active(self):
        print(f"Robot {self.id}: Chasing Ball")

    def idle(self):
        print(f"Robot {self.id}: Waiting for Action")

    def assign_behaviour(self):
        self.behaviour = "player"