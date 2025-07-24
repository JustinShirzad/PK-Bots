from .robot import Robot

class Goalie(Robot):
    def __init__(self, id):
        super().__init__(id)
        super().assign_behaviour()

    def active(self):
        # Get robot position
        # Get ball position
        # Calculate relative distance to ball
        # Generate velocity based on relative distance
        # Move towards the ball
        print(f"Robot {self.id}: Guarding Goal")

    def idle(self):
        print(f"Robot {self.id}: Waiting for Action")

    def assign_behaviour(self):
        self.behaviour = "goalie"