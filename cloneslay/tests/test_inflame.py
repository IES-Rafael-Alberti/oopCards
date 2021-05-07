from cloneslay.actor import Actor
from cloneslay.cards.inflame import Inflame
from cloneslay.cards.strike import Strike


def test_inflame():
    my_inflame = Inflame()
    my_strike = Strike()
    actor1 = Actor([my_inflame, my_strike, my_strike])
    actor2 = Actor([])
    my_strike.activate(actor1, actor2)
    assert actor2.live_points == 293
    my_inflame.activate(actor1, actor1)
    assert actor1.strength == 2
    my_strike.activate(actor1, actor2)
    assert actor2.live_points == 284
