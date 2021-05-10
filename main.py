from game.game import Game
from game.deck_lab import DeckLab
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        myGame = DeckLab()
    else:
        myGame = Game()
    myGame.game_loop()







