from cloneslay.card import Card


class BodySlam(Card):
    def __init__(self):
        super().__init__("Body Slam", 1, "attack", "Deal damage equal.to your block", "bodyslam.png")

    def activate(self, actor, goal):
        Card.attack(actor.block_points, actor, goal)
        # Card.discard_used_card("Body Slam", actor)