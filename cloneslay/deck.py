class Deck:
    def __init__(self, cards=None):
        self.cards = [] if cards is None else cards

    def size(self):
        return len(self.cards)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += str(card) + "\n"
        return result