from cloneslay.card import Card


class BloodLetting (Card):
    def __init__(self):
        super().__init__("BloodLetting", 0, "Skill", "Lose 3 HP.Gain 2 energy", "Bloodletting.png")

    # activate must have 2 arguments, you can make goal optional with default: goal=None
    def activate(self, actor, goal=None):
        actor.live_points = actor.live_points - 3
        actor.energy = actor.energy + 2
        #Card.discard_used_card("Defend", actor)
