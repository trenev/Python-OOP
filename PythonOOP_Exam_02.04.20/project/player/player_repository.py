from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    @property
    def players_names(self):
        return [player.username for player in self.players]

    def add(self, player: Player):
        if player.username in self.players_names:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player_name: str):
        if player_name == "":
            raise ValueError("Player cannot be an empty string!")
        self.players.remove(self.find(player_name))
        self.count -= 1

    def find(self, username: str):
        return [player for player in self.players if player.username == username][0]
