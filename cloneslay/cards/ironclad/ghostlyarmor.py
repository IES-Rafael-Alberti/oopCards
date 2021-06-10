from cloneslay.card import Card


class GhostlyArmor(Card):
    def __init__(self):
        super().__init__("GhostlyArmor", 1, "Skill", "Ethereal. Gain 10 Block.", "GhostlyArmor.png",
                         rarity="uncommon", ethereal=True)

    def activate(self, actor, goal):
        actor.block_points += 10
        # Card.exhaust_a_card("Carnage", actor)