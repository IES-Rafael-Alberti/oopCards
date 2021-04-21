from cloneslay.card import Card


class Defense (Card):
    def __init__(self):
        super().__init__("Defend_card", 2, "Skill", "Gain 5 Block", None)

    def activate(self, actor):
        self.block(5, actor)