from .game.game import *


class Model:

    def __init__(self):
        self.game = Game()

    def refresh(self):
        self.game.refresh()


