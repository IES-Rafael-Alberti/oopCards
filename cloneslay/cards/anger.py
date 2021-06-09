from cloneslay.card import Card


class Anger(Card):
    def __init__(self):
        super().__init__("Anger", 0, "attack", "Deal 6 damage.Add a copy of this card.into your discard pile", "strike.png")

    def activate(self, actor, goal):
        Card.attack(6, actor, goal)
        actor.discarded.add_card(Card.get_card("Anger"))
        # Card.discard_used_card("Strike", actor)