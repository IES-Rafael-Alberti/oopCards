from cloneslay.card import Card
import random

class PommelStrike(Card):
    def __init__(self):
        super().__init__("PommelStrike", 1, "attack", "Deal 9 damage.Draw 1 card", "Pommel_Strike.png",
                         rarity="common")

    def activate(self, actor, goal):
        Card.attack(9, actor, goal)
        actor.hand.add_card(random.choice(actor.deck))
