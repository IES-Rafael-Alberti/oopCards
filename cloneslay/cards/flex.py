from cloneslay.card import Card
from cloneslay.commands import endturn


class Flex(Card):
    def __init__(self):
        super().__init__("Flex", 0, "skill", "Gain 2 Strength.At the end of.your turn.lose 2 Strength", "barricade.png",
                         rarity="common")

    def activate(self, actor, goal=None):
        Card.add_strength(2, actor)
        actor.add_command(endturn.ReduceStrength(2))