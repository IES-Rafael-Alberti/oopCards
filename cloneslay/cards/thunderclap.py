from cloneslay.card import Card


class Thunderclap(Card):
    def __init__(self):
        super().__init__("Thunderclap", 1, "attack", "Deal 4 damage and.apply 1 vulnerable. to ALL enemies", "bash.png",
                         rarity="common")

    def activate(self, actor, goal):
        Card.attack(4, actor, goal)
        Card.add_vulnerable(1, goal)
