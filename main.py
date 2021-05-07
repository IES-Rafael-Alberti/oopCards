from game.game import Game
from game.deck_lab import DeckLab
import sys


if __name__ == '__main__':
    if sys.argv:
        myGame = DeckLab()
    else:
        myGame = Game()
    myGame.game_loop()







