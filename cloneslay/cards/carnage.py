from cloneslay.card import Card


class Carnage(Card):
    def __init__(self):
        super().__init__("Carnage", 2, "attack", "Ethereal. Deal 20 damage.", None, True, True)

    def activate(self, actor, goal):
        Card.attack(20, actor, goal)
        # Card.exhaust_a_card("Carnage", actor)