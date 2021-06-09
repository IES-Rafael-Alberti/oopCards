from cloneslay.commands.command import Command


class Default(Command):
    command_key = "endturn"

    def execute(self, actor):
        pass


class ReduceStrength(Default):

    def __init__(self, quantity):
        Default.__init__()
        self.stable = False
        self.quantity = quantity

    def execute(self, actor):
        actor.strength -= self.quantity