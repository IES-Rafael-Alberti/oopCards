from cloneslay.actor import Actor
from cloneslay.cards.bodyslam import BodySlam

def test_strike():
    my_bodyslam = BodySlam()
    actor1 = Actor([my_bodyslam])
    actor2 = Actor([])
    my_bodyslam.activate(actor1, actor2)
    assert actor2.live_points == 50
    actor1.block(10)
    actor2.block(2)
    my_bodyslam.activate(actor1, actor2)
    assert actor2.live_points == 42