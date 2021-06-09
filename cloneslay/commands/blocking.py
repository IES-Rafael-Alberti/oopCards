from cloneslay.commands.command import Command


class Default(Command):
    command_key = "blocking"

    def execute(self, actor):
        actor.block_points = 0

class KeepBlock(Default):
    def execute(self, actor):
        pass
