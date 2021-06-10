from cloneslay.card import Card


class TwinStrike(Card):
    def __init__(self):
        super().__init__("Twin Strike", 1, "attack", "Deal 5 damage.twice", "bash.png",
                         rarity="common")

    def activate(self, actor, goal):
        Card.attack(5, actor, goal)
        Card.attack(5, actor, goal)
