from cloneslay.actor import Actor
from cloneslay.cards.carnage import JoseJavier_Corrigiendo
from cloneslay.cards.defense import Defense

def test_strike():
    my_defense = Defense()
    my_carnage = JoseJavier_Corrigiendo()
    actor1 = Actor([my_carnage, my_defense])
    actor2 = Actor([])
    my_carnage.activate(actor1, actor2)
    assert actor2.live_points == 30
    my_defense.activate(actor2)
    assert actor2.block_points == 5
    my_carnage.activate(actor1, actor2)
    assert actor2.block_points == 0
    assert actor2.live_points == 15