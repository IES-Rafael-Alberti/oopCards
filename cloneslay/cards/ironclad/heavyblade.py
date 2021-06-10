from cloneslay.card import Card



class HeavyBlade(Card):
    def __init__(self):
        super().__init__("Heavy Blade", 2, "attack", "Deal 14 damage.Strength affects Heavy.Blade 3 times",
                         "barricade.png", rarity="common")

    def activate(self, actor, goal=None):
        Card.attack(14, actor, goal, 3)
