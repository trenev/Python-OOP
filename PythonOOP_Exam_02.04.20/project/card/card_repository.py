from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    @property
    def cards_names(self):
        return [card.name for card in self.cards]

    def add(self, card: Card):
        if card.name in self.cards_names:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card_name: str):
        if card_name == "":
            raise ValueError("Card cannot be an empty string!")
        self.cards.remove(self.find(card_name))
        self.count -= 1

    def find(self, name: str):
        return [card for card in self.cards if card.name == name][0]
