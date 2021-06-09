from cloneslay.card import Card


class Havoc(Card):
    def __init__(self):
        super().__init__("Havoc", 1, "skill", "Play the top card.of your draw pile.and Exhaust it", "barricade.png",
                         rarity="common")

    def activate(self, actor, goal):
        card = actor.draw.get(1)
        card.exhaust = True
        card.activate(actor, goal)
