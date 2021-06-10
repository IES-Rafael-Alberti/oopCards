from cloneslay.card import Card
import random

class Survivor(Card):
    def __init__(self):
        super().__init__("Survivor", 1, "Skill", "Gain 8 Block.Discard 1 card", "Defense.png",
                         rarity="starter")

    def activate(self, actor, goal):
        Card.attack(7, actor, goal)
        actor.hand.delete_card(random.choice(actor.hand.cards))
