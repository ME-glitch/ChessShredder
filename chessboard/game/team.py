from .player.player import *


class Team:

    def __init__(self, color):
        self.color = color
        self.player = Player(color)
        self.initiate_pieces()

    def initiate_pieces(self):
        self.player.initiate_pieces()

    def get_piece_on(self, pos):
        return self.player.get_piece_on(pos)

    def get_all_positions(self):
        return self.player.get_all_positions()

    def generate_team_possible_moves(self, allPositions):
        return self.player.generate_team_possible_moves(allPositions)

