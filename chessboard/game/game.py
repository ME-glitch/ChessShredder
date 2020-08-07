from .team import *


class Game:

    def __init__(self):
        self.whiteTeam = Team(WHITE)
        self.blackTeam = Team(BLACK)
        self.allPositions = []
        self.get_all_positions_of_pieces()
        self.generate_set_of_all_possible_moves()

    def refresh(self):
        self.get_all_positions_of_pieces()
        self.generate_set_of_all_possible_moves()

    def get_all_positions_of_pieces(self):
        self.allPositions = []
        whitePosition = self.whiteTeam.get_all_positions()
        blackPosition = self.blackTeam.get_all_positions()

        for p in whitePosition:
            self.allPositions.append(p)
        for p in blackPosition:
            self.allPositions.append(p)

        return self.allPositions

    def has_piece_on(self, pos):
        has_position, piece = self.whiteTeam.get_piece_on(pos)
        if has_position:
            return has_position, piece
        else:
            return self.blackTeam.get_piece_on(pos)

    def generate_set_of_all_possible_moves(self):
        self.whiteTeam.generate_team_possible_moves(self.allPositions)
        self.blackTeam.generate_team_possible_moves(self.allPositions)
        pass
