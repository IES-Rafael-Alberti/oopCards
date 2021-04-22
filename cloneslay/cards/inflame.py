from cloneslay.card import Card


class Inflame(Card):
    def __init__(self):
        super().__init__("Inflame", 1, "power", "Gain 2 Strength", None)

    def activate(self, actor, goal):
        actor.add_strength(self, 2)
