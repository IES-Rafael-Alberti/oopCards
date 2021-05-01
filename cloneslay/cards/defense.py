from cloneslay.card import Card


class Defense (Card):
    def __init__(self):
        super().__init__("Defend_card", 1, "Skill", "Gain 5 Block", "defense.png")

    # activate must have 2 arguments, you can make goal optional with default: goal=None
    def activate(self, actor, goal=None):
        Card.block(5, actor)
        # Card.discard_used_card("Defend_card", actor)
