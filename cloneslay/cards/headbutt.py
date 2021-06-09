from cloneslay.card import Card


class Headbutt(Card):
    def __init__(self):
        super().__init__("Headbutt", 0, "attack", "Deal 9 damage.Place a card from.your discard pile.on top of your."
                                                  "draw pile",
                         "barricade.png", rarity="common")

    def activate(self, actor, goal):
        Card.attack(9, actor, goal)
        if actor.discarded.cards:
            actor.discarded.shuffle()
            card = actor.discarded.get(1)
            actor.discarded.transfer_card(card, actor.draw)
