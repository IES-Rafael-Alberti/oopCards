from cloneslay.card import Card


class IronWave(Card):
    def __init__(self):
        super().__init__("Iron Wave", 1, "attack", "Gain 5 block.deal 5 damage", "")

    def activate(self, actor, goal):
        Card.attack(5, actor, goal)
        actor.block(self, 5)
