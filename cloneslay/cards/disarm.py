from cloneslay.card import Card


class Disarm (Card):
    def __init__(self):
        super().__init__("Disarm", 1, "Skill", "Enemy loses 2.Strenght.Exhaust", "Disarm.png",
                         rarity='Uncommon', exhaust=True)

    # activate must have 2 arguments, you can make goal optional with default: goal=None
    def activate(self, actor, goal):
        goal.strength -= 2

        #Card.discard_used_card("Defend", actor)
