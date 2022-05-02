class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player):
        filtered_player = [element for element in self.players if element == player]
        if not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        if filtered_player:
            return f"Player {player.name} is already in the guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        filtered_player = [element for element in self.players if element.name == player_name]
        if not filtered_player:
            return f"Player {player_name} is not in the guild."
        filtered_player[0].guild = "Unaffiliated"
        self.players.remove(filtered_player[0])
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for element in self.players:
            result += f"{element.player_info()}"
        return result

