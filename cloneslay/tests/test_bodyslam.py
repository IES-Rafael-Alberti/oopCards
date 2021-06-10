from cloneslay.actor import Actor
from cloneslay.cards.ironclad.bodyslam import BodySlam


def test_bodyslam():
    my_bodyslam = BodySlam()
    actor1 = Actor([my_bodyslam, my_bodyslam])
    actor2 = Actor([])
    my_bodyslam.activate(actor1, actor2)
    assert actor2.live_points == 300
    actor1.block(10)
    actor2.block(2)
    my_bodyslam.activate(actor1, actor2)
    assert actor2.live_points == 292
