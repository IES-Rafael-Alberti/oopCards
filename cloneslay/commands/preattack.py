from cloneslay.commands.command import Command


class Default(Command):
    command_key = "preattack"

    def execute(self, actor):
        pass


class IncreaseStrength(Default):

    def __init__(self, times):
        Default.__init__()
        self.stable = False
        self.times = times

    # TODO: def execute(self, actor):
        # damage += actor.strength *