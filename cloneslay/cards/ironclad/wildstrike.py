from cloneslay.card import Card
from cloneslay.cards.ironclad.wound import Wound
from random import randrange


class WildStrike(Card):
    def __init__(self):
        super().__init__("Wild Strike", 1, "attack", "Deal 12 damage.Shuffle a Wound into.your draw pile", "bash.png",
                         rarity="common")

    def activate(self, actor, goal):
        Card.attack(12, actor, goal)
        actor.draw.cards.insert(randrange(len(actor.draw.cards), Wound()))
