from cloneslay.actor import Actor
from cloneslay.cards.strike import Strike


def test_strike():
    my_strike = Strike()
    actor1 = Actor([my_strike])
    actor2 = Actor([])
    my_strike.activate(actor1, actor2)
    assert actor2.live_points == 43
    actor2.block(10)
    my_strike.activate(actor1, actor2)
    assert actor2.block_points == 3
    my_strike.activate(actor1, actor2)
    assert actor2.block_points == 0
    assert actor2.live_points == 39
