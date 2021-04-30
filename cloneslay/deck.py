import random


class Deck:
    def __init__(self, cards=None):
        if isinstance(cards, Deck):
            self.cards = cards.cards
        else:
            self.cards = [] if cards is None else cards

    def get(self, number):
        if number >= self.size():
            result = Deck(self.cards)
            self.cards = []
        else:
            result = Deck(self.cards[:number])
            self.cards = self.cards[number:]
        return result

    def add(self, other):
        self.cards.extend(other.cards)

    def size(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def get_one_card(self, card_name):
        for i in self.cards:
            if card_name == i.name:
                return i
        return None

    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card) + "\n"
        return result