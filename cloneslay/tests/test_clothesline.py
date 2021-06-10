from cloneslay.actor import Actor
from cloneslay.cards.ironclad.clothesline import Clothesline
from cloneslay.cards.ironclad.strike import Strike


def test_strike():
    my_strike = Strike()
    my_Clothesline = Clothesline()
    actor1 = Actor([my_strike, my_strike, my_Clothesline])
    actor2 = Actor([my_strike])
    my_Clothesline.activate(actor1, actor2)
    assert actor2.live_points == 288
    assert actor2.weak == 2
    actor1.end_turn()
    actor2.init_turn()
    my_strike.activate(actor2,actor1)
    assert actor1.live_points == 294
    assert actor2.weak == 1

