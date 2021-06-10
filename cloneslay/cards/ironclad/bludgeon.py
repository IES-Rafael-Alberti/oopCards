from cloneslay.card import Card


class Bludgeon (Card):
    def __init__(self):
        super().__init__("Bludgeon", 3, "attack", "Deal 32 damage", "bludgeon.png",
                         rarity = "Rare")

    def activate(self, actor, goal):
        Card.attack(32, actor, goal)
        # Card.discard_used_card("Bludgeon", actor)