from chessboard.configuration import *
from ..pieces.pawn import *
from ..pieces.rook import *
from ..pieces.queen import *
from ..pieces.bishop import *
from ..pieces.king import *
from ..pieces.knight import *


class Player:

    def __init__(self, color):
        self.color = color
        self.pawns = []
        self.knights = []
        self.rooks = []
        self.king = []
        self.queens = []
        self.bishops = []
        self.positions = []

    def initiate_pieces(self):
        self.initiate_pawns()
        self.initiate_rooks()
        self.initiate_bishops()
        self.initiate_knights()
        self.initiate_royals()

    def initiate_pawns(self):
        if self.color == WHITE:
            config = WHITE_PAWN
        else:
            config = BLACK_PAWN

        for p in range(0, NUMBER_OF_STARTING_PAWNS):
            self.pawns.append(Pawn(config, p))

    def initiate_rooks(self):
        if self.color == WHITE:
            config = WHITE_ROOKS
        else:
            config = BLACK_ROOKS

        for p in range(0, NUMBER_OF_STARTING_RKB):
            self.rooks.append(Rook(config, p))

    def initiate_bishops(self):
        if self.color == WHITE:
            config = WHITE_BISHOPS
        else:
            config = BLACK_BISHOPS

        for p in range(0, NUMBER_OF_STARTING_RKB):
            self.bishops.append(Bishop(config, p))

    def initiate_knights(self):
        if self.color == WHITE:
            config = WHITE_KNIGHTS
        else:
            config = BLACK_KNIGHTS

        for p in range(0, NUMBER_OF_STARTING_RKB):
            self.knights.append(Knight(config, p))

    def initiate_royals(self):
        if self.color == WHITE:
            configQueen = WHITE_QUEEN
            configKing = WHITE_KING
        else:
            configQueen = BLACK_QUEEN
            configKing = BLACK_KING

        self.queens.append(Queen(configQueen, 0))
        self.king.append(King(configKing, 0))

    def get_piece_on(self, position):
        for pawn in self.pawns:
            if pawn.get_position() == position:
                return True, pawn
        for rook in self.rooks:
            if rook.get_position() == position:
                return True, rook
        for knight in self.knights:
            if knight.get_position() == position:
                return True, knight
        for bishop in self.bishops:
            if bishop.get_position() == position:
                return True, bishop
        for queen in self.queens:
            if queen.get_position() == position:
                return True, queen
        if self.king[0].get_position() == position:
            return True, self.king[0]

        return False, None

    def generate_team_possible_moves(self, allPositions):

        self.get_pawns_moves(allPositions)
        self.get_rooks_moves(allPositions)
        self.get_knights_moves(allPositions)
        self.get_bishops_moves(allPositions)
        self.get_queen_moves(allPositions)
        self.get_king_moves(allPositions)
        pass

    def get_pawns_moves(self, allPositions):
        for pawn in self.pawns:
            pawn.generate_possible_moves(allPositions)
        pass

    def get_rooks_moves(self, allPositions):
        for rook in self.rooks:
            rook.generate_possible_moves(allPositions)
        pass

    def get_knights_moves(self, allPositions):
        for knight in self.knights:
            knight.generate_possible_moves(allPositions)
        pass

    def get_bishops_moves(self, allPositions):
        for bishop in self.bishops:
            bishop.generate_possible_moves(allPositions)

    def get_queen_moves(self, allPositions):
        for queen in self.queens:
            queen.generate_possible_moves(allPositions)
        pass

    def get_king_moves(self, allPositions):
        self.king[0].generate_possible_moves(allPositions)
        pass

    def get_all_positions(self):
        positions = []
        self.positions.clear()
        for p in self.pawns:
            positions.append(p.get_position())
            self.positions.append(p.get_position())
        for k in self.knights:
            positions.append(k.get_position())
            self.positions.append(k.get_position())
        for r in self.rooks:
            positions.append(r.get_position())
            self.positions.append(r.get_position())
        for b in self.bishops:
            positions.append(b.get_position())
            self.positions.append(b.get_position())
        for q in self.queens:
            positions.append(q.get_position())
            self.positions.append(q.get_position())
        for k in self.king:
            positions.append(k.get_position())
            self.positions.append(k.get_position())
        return positions
        pass
