from cloneslay.card import Card


class HemoKinesis(Card):
    def __init__(self):
        super().__init__("HemoKinesis", 1, "Attack", "Lose 2 HP.Deal 15 damage", "hemokinesis.png",
                         rarity='Uncommon')

    def activate(self, actor, goal):
        actor.live_points -=2
        Card.attack(15, actor, goal)
        # Card.discard_used_card("Strike", actor)