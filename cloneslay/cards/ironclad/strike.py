from cloneslay.card import Card


class Strike(Card):
    def __init__(self):
        super().__init__("Strike", 1, "attack", "Attack with 7 damage", "strike.png")

    def activate(self, actor, goal):
        Card.attack(7, actor, goal)
        # Card.discard_used_card("Strike", actor)