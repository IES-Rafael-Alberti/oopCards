from cloneslay.card import Card


class Wound(Card):
    def __init__(self):
        super().__init__("Wound", 0, "status", "Unplayable", "bash.png", rarity="common")

    def preconditions(self,actor):
        return False

    def activate(self, actor, goal):
        pass