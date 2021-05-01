from cloneslay.card import Card


class SwordBoomerang(Card):
    def __init__(self):
        super().__init__("Sword_boomerang o Batmerang", 1, "attack",
                         "Deal 3 damage to a random enemy 3(4) times.", "swordboomerang.png")

    def activate(self, actor, goal):
        for _ in range(3):
            Card.attack(3, actor, goal)
        # Card.discard_used_card("Sword_boomerang o Batmerang", actor)