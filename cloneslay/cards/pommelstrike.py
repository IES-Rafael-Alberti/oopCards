from cloneslay.card import Card


class PommelStrike(Card):
    def __init__(self):
        super().__init__("Pommel Strike", 1, "attack", "Deal 9 damage.Draw 1 card", "bash.png",
                         rarity="common")

    def activate(self, actor, goal):
        Card.attack(9, actor, goal)
        actor.hand.add_card(actor.draw.get(1))
