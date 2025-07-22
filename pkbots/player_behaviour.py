from .robot import Robot

class Player(Robot):
    def __init__(self, id):
        super().__init__(id)
        super().assign_behaviour()

    def run(self):
        print(f"Robot {self.id}: Chasing Ball")

    def assign_behaviour(self):
        self.behaviour = "player"