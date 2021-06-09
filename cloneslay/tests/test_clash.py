from cloneslay.actor import Actor
from cloneslay.cards.strike import Strike
from cloneslay.cards.clash import Clash
from cloneslay.cards.defense import Defense


def test_Clash():
    my_Clash = Clash()
    my_strike = Strike()
    my_Defense = Defense()
    actor1 = Actor([my_strike, my_strike, my_strike, my_Clash])
    actor2 = Actor([])
    my_Clash.preconditions(actor1)
    my_Clash.activate(actor1, actor2)
    assert actor2.live_points == 286


def test_Clash_Use():
    my_Clash = Clash()
    my_strike = Strike()
    my_Defense = Defense()
    actor1 = Actor([my_strike, my_strike, my_strike, my_Clash,my_Defense])
    actor2 = Actor([])
    my_Clash.preconditions(actor1)
    my_Clash.activate(actor1, actor2)
    assert actor2.live_points == 300
