from cloneslay.card import Card


class Strike(Card):
    def __init__(self):
        super().__init__("Strike", 1, "attack", "Deal 6 damage", "strike.png",
                            rarity="starter")

    def activate(self, actor, goal):
        Card.attack(7, actor, goal)
        # Card.discard_used_card("Strike", actor)