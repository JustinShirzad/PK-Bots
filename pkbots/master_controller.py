from .player_behaviour import Player
from .goalie_behaviour import Goalie

class MasterController:
    def __init__(self):
        self.robots = self.initialize_robots()
    
    def initialize_robots(self):
        robots = []

        # Initialise a Player and a Goalie robot
        player_robot = Player(1)
        goalie_robot = Goalie(2)
        
        # Add them to the list of robots
        robots.append(player_robot)
        robots.append(goalie_robot)

        return robots
    
    def update(self):
        for robot in self.robots:
            robot.active()
