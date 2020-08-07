from .piece import Piece
from PIL import Image, ImageTk
from chessboard.configuration import *
from chessboard.utils.Utils import Utils


class King(Piece):

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

        direction = [-1, -7, -8, -9, 1, 7, 8, 9]

        for d in direction:
            newPosition = self.pos + d
            if 65 > newPosition > 0 and not Utils.isCollision(newPosition, allPositions):
                self.possiblePositions.append(newPosition)

    def get_possible_moves(self):
        return self.possiblePositions

