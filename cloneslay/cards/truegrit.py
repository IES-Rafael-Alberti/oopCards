import random

from cloneslay.card import Card


class TrueGrit (Card):
    def __init__(self):
        super().__init__("TrueGrit", 1, "Skill", "Gain 7 Block. Exhaust a random.card in your hand", "truegrit.png",
                         rarity = "Common")

    # activate must have 2 arguments, you can make goal optional with default: goal=None
    def activate(self, actor, goal=None):
        Card.block(7, actor)
        random_card = random.choice(actor.hand.cards)
        actor.exhaust_card(random_card)
        #Card.discard_used_card("TrueGrit", actor)
