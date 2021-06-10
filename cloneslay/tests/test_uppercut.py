from cloneslay.actor import Actor
from cloneslay.cards.ironclad.strike import Strike
from cloneslay.cards.ironclad.uppercut import Uppercut


def test_strike():
    my_uppercut = Uppercut()
    my_strike = Strike()

    actor1 = Actor([my_strike, my_strike, my_uppercut])
    actor2 = Actor([my_strike])
    my_uppercut.activate(actor1, actor2)

    assert actor2.live_points == 287
    my_strike.activate(actor1, actor2)
    assert actor2.live_points == 277
    assert actor2.weak == 1
    assert actor2.vulnerable == 1

    actor1.end_turn()
    actor2.init_turn()
    my_uppercut.activate(actor2, actor1)
    assert actor1.weak == 1
    assert actor1.vulnerable == 1
    assert actor1.live_points == 287
    assert actor2.weak == 0
    assert actor2.vulnerable == 0

