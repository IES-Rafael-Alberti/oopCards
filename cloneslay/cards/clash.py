import random

from cloneslay.card import Card


class Clash (Card):
    def __init__(self):
        super().__init__("Clash", 1, "Attack", "Can only be played if.every card in your.hand is an Attack.Deal 14 damage", "clash.png",

                         rarity= "Common")


    # activate must have 2 arguments, you can make goal optional with default: goal=None
    """def preconditions(self,actor):
        for card in actor.hand.cards:
            if card.card_type.lower != "attack":
                actor.energy += self.energy
                return False
        return  True
    """
    def activate(self, actor, goal):
        Card.attack(14, actor, goal)





    # Card.discard_used_card