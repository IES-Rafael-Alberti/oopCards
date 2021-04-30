from cloneslay.actor import Actor
from cloneslay.cards.strike import Strike
from cloneslay.cards.defense import Defense

def test_strike():
    my_defense = Defense()
    my_strike = Strike()
    actor1 = Actor([my_strike, my_strike])
    actor2 = Actor([my_defense])
    my_strike.activate(actor1, actor2)
    assert actor2.live_points == 43
    my_defense.activate(actor2)
    assert actor2.block_points == 5
    my_strike.activate(actor1, actor2)
    assert actor2.block_points == 0
    assert actor2.live_points == 41