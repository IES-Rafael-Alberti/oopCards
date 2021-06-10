from cloneslay.actor import Actor
from cloneslay.cards.ironclad.bash import Bash


def test_bash():
    my_bash = Bash()
    actor1 = Actor([my_bash, my_bash, my_bash])
    actor2 = Actor([])
    my_bash.activate(actor1, actor2)
    assert actor2.live_points == 292
    assert actor2.vulnerable == 2
    actor2.block(10)
    my_bash.activate(actor1, actor2)
    assert actor2.live_points == 290
    assert actor2.block_points == 0
    my_bash.activate(actor1, actor2)
    assert actor2.live_points == 278
    assert actor2.block_points == 0
