from cloneslay.actor import Actor
from cloneslay.cards.strike import Strike
from cloneslay.cards.bludgeon import Bludgeon


def test_strike():
    my_strike = Strike()
    my_bludgeon = Bludgeon()
    actor1 = Actor([my_bludgeon, my_strike, my_strike])
    actor2 = Actor([])
    my_bludgeon.activate(actor1, actor2)
    assert actor2.live_points == 268
