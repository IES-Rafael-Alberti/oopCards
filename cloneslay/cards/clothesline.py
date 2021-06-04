from cloneslay.card import Card


class Clothesline(Card):
    def __init__(self):
        super().__init__("Clothesline", 2, "Attack", "Deal 12 damage.Apply 2 Weak", "clothesline.png",
                         rarity= "Common")

    def activate(self, actor, goal):
        Card.attack(12, actor, goal)
        goal.add_weakness(2)
        # Card.discard_used_card("Str