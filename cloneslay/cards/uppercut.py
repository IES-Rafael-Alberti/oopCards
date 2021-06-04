from cloneslay.card import Card


class Uppercut(Card):
    def __init__(self):
        super().__init__("Uppercut", 2, "Attack", "Deal 13 damage.Apply 1 Weak.Apply 1 Vulnerable", "Uppercut.png",
                         rarity= "Uncommon")

    def activate(self, actor, goal):
        Card.attack(13, actor, goal)
        goal.add_weakness(1)
        self.add_vulnerable(1,goal)
