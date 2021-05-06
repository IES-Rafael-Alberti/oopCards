from cloneslay.commands.command import Command


class Default(Command):
    type = "posthand"

    def execute(self, actor):
        pass


class CorruptionCommand(Default):
    def execute(self, actor):
        for card in actor.hand.cards:
            if card.card_type.lower() == "skill":
                card.energy = 0
                card.exhaust = True
