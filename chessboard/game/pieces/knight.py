from .piece import Piece
from PIL import Image, ImageTk
from chessboard.configuration import *
from chessboard.utils.Utils import Utils


class Knight(Piece):

    def __init__(self, configDic, num):
        self.color = configDic['color']
        self.fileName = configDic['fileName']
        #TODO: not every piece needs to reference the picture.
        self.image = Image.open(IMG_LOCATION + self.fileName)
        print(IMG_LOCATION + self.fileName)
        print(self.image)
        self.photo = ImageTk.PhotoImage(self.image)
        self.pos = configDic['startLocations'][num]
        self.possiblePositions = []

    def get_photo(self):
        return self.photo

    def set_in_play(self, inPlay: bool):
        pass

    def is_in_play(self) -> bool:
        pass

    def set_position(self, pos):
        self.pos = pos

    def get_position(self):
        return self.pos

    def set_photo(self, photo):
        pass

    def generate_possible_moves(self, allPositions):
        self.possiblePositions.clear()
        positionChecks = [-6, 6, -10, 10, -15, 15, -17, 17]

        for x in positionChecks:
            newPosition = self.pos + x
            if 0 < newPosition < 65 and not Utils.isCollision(newPosition, allPositions):
                self.possiblePositions.append(newPosition)

    def get_possible_moves(self):
        return self.possiblePositions
        pass
