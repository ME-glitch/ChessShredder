from .piece import Piece
from PIL import Image, ImageTk
from chessboard.configuration import *
from chessboard.utils.Utils import Utils

class Pawn(Piece):

    def __init__(self, configDic, num):
        self.color = configDic['color']
        self.fileName = configDic['fileName']
        #TODO: not every piece needs to reference the picture.
        self.image = Image.open(IMG_LOCATION + self.fileName)
        print(IMG_LOCATION + self.fileName)
        print(self.image)
        self.photo = ImageTk.PhotoImage(self.image)
        self.pos = configDic['startLocations'][num]
        self.firstMove = False
        self.possiblePositions = []

    def get_photo(self):
        return self.photo

    def set_in_play(self, inPlay: bool):
        pass

    def is_in_play(self) -> bool:
        pass

    def set_position(self, pos):
        self.firstMove = True
        self.pos = pos

    def get_position(self):
        return self.pos

    def set_photo(self, photo):
        pass

    def generate_possible_moves(self, allPositions):
        self.possiblePositions.clear()

        if not self.firstMove:
            if self.color == BLACK:
                newPos = self.pos + 8
                if not Utils.isCollision(newPos, allPositions) and not Utils.isCollision(newPos + 8, allPositions):
                    self.possiblePositions.append(self.pos + 8)
                    self.possiblePositions.append(self.pos + 16)
            else:
                newPos = self.pos - 8
                if not Utils.isCollision(newPos, allPositions) and not Utils.isCollision(newPos - 8, allPositions):
                    self.possiblePositions.append(self.pos - 8)
                    self.possiblePositions.append(self.pos - 16)
        else:
            if self.color == BLACK:
                newPos = self.pos + 8
                if not Utils.isCollision(newPos, allPositions):
                    self.possiblePositions.append(newPos)
            else:
                newPos = self.pos - 8
                if not Utils.isCollision(newPos, allPositions):
                    self.possiblePositions.append(self.pos - 8)

    def get_possible_moves(self):
        return self.possiblePositions
