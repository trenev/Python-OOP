from project.player.player import Player


class Beginner(Player):
    initial_health_points = 50

    def __init__(self, username: str):
        super().__init__(username, Beginner.initial_health_points)
