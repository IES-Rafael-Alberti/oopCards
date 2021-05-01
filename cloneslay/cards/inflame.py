from cloneslay.card import Card


class Inflame(Card):
    def __init__(self):
        super().__init__("Inflame", 1, "power", "Gain 2 Strength", None)

    def activate(self, actor, goal):
        # self is taken with method calling, it is wrong to send self here because it is a Card
        # try not to call Actor directly from cards, use Card class instead
        Card.add_strength(2, actor)
        Card.discard_used_card("Inflame", actor)