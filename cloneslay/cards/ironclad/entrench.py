from cloneslay.card import Card


class Entrench(Card):
    def __init__(self):
        super().__init__("Entrench", 2, "Skill", "Double your Block","entrench.png",
                         rarity='Uncommon')

    def activate(self, actor, goal = None):
        actor.block_points *=2
        # Card.discard_used_card("Strike", actor)