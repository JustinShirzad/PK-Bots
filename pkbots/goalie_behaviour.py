from .robot import Robot

class Goalie(Robot):
    def __init__(self, id):
        super().__init__(id)
        super().assign_behaviour()

    def run(self):
        print(f"Robot {self.id}: Guarding Goal")

    def assign_behaviour(self):
        self.behaviour = "goalie"