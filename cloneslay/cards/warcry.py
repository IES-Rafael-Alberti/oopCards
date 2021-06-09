import random

from cloneslay.card import Card


class Warcry(Card):
    def __init__(self):
        super().__init__("Warcry", 0, "skill", "Draw 1 card.Place a card from.your hand on top.of your draw pile."
                                               "Exhaust.",
                         "bash.png", exhaust=True, rarity="common")

    def activate(self, actor, goal):
        actor.hand.add_card(actor.draw.get(1))
        selected_card = actor.hand.choose_card()
        # TODO: