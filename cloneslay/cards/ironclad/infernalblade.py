from cloneslay.card import Card
import random

class InfernalBlade(Card):
    def __init__(self):
        super().__init__("InfernalBlade", 1, "Skill", "Add a random Attack.into your hand. its costs 0 this turn.Exhaust", "infernalblade.png",
                         rarity="uncommon", exhaust=True)

    def activate(self, actor, goal):
        attack = []
        for card in actor.draw.cards:
            if card.card_type.lower() == 'attack':
                attack.append(card)
        actor.draw.transfer_card(random.choice(actor.draw.cards),actor.hand)

