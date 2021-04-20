from cloneslay.card import Card


class Strike(Card):
    def __init__(self):
        super().__init__("Strike", "attack", "Attack with 7 damage", None)

    def activate(self, actor, goal):
        self.attack(7, actor, goal)
