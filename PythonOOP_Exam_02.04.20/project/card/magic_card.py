from project.card.card import Card


class MagicCard(Card):
    initial_damage_points = 5
    initial_health_points = 80

    def __init__(self, name: str):
        super().__init__(name, MagicCard.initial_damage_points, MagicCard.initial_health_points)
