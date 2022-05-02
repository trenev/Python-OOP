from project.card.card import Card


class TrapCard(Card):
    initial_damage_points = 120
    initial_health_points = 5

    def __init__(self, name: str):
        super().__init__(name, TrapCard.initial_damage_points, TrapCard.initial_health_points)
