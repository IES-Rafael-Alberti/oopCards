from cloneslay.card import Card
import random

class Backflip (Card):
    def __init__(self):
        super().__init__("Backflip", 1, "Skill", "Gain 5 Block.Draw 2 cards", "defense.png",
                         rarity="common")


    def activate(self, actor, goal=None):
        Card.block(5, actor)
        for i in range(0, 1):
            actor.draw.transfer_card(random.choice(actor.draw.cards),actor.hand)
