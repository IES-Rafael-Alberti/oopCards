from cloneslay.card import Card
from cloneslay.commands import posthand


class Corruption(Card):
    def __init__(self):
        super().__init__("Corruption", 3, "power", "Skills cost 0.Whenever you play a.Skill, Exhaust it",
                         "corruption.png", False, False)

    def activate(self, actor, goal):
        actor.add_command(posthand.CorruptionCommand())
