from cloneslay.card import Card


class Sword_boomerang(Card):
    def __init__(self):
        super().__init__("Sword_boomerang o Batmerang", 1, "attack", "Deal 3 damage to a random enemy 3(4) times.", None)

    def activate(self, actor, goal):
        Card.attack(9, actor, goal)