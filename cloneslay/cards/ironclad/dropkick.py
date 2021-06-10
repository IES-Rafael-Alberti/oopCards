from cloneslay.card import Card
import random

class DropKick(Card):
    def __init__(self):
        super().__init__("DropKick", 1, "Attack", "Deal 5 damage.If the enemy has Vulnerable.gain 1 energy and.draw 1 card","dropkick.png",
                         rarity='Uncommon')

    def activate(self, actor, goal):
        Card.attack(5, actor, goal)
        if goal.vulnerable > 0:
            actor.energy +=1
            actor.draw.transfer_card(random.choice(actor.draw.cards),actor.hand)
        # Card.discard_used_card("Strike", actor)