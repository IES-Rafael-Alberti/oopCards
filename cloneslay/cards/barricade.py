from cloneslay.card import Card
from cloneslay.commands import blocking


class Barricade(Card):
    def __init__(self):
        super().__init__("Barricade", 3, "power", "Block is not removed.at the start of.your turn", "barricade.png")

    def activate(self, actor, goal):
        actor.add_command(blocking.KeepBlock())
        # Card.discard_used_card("Strike", actor)