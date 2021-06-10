from cloneslay.card import Card
import random

class DaggerThrow(Card):
    def __init__(self):
        super().__init__("DaggerThrow", 1, "attack", "Deal 9 damage.Draw 1 card.Discard 1 card", "strike.png",
                            rarity="starter")

    def activate(self, actor, goal):
        Card.attack(9, actor, goal)
        actor.hand.add_card(random.choice(actor.deck))
        actor.hand.delete_card(random.choice(actor.hand.cards))
        # Card.discard_used_card("Strike", actor)