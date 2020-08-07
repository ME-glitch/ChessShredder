from .piece import Piece
from PIL import Image, ImageTk
from chessboard.configuration import *
from chessboard.game.coordinates.position import Position
from chessboard.utils.Utils import Utils


class Rook(Piece):

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

    # TODO make more efficient
    def generate_possible_moves(self, allPositions):
        self.possiblePositions.clear()

        ## vertical
        for x in range(0, NUMBER_OF_COLUMNS):
            newPosition = self.pos + 8*x

            if newPosition < 65 and not Utils.isCollision(newPosition, allPositions):
                self.possiblePositions.append(newPosition)

        for x in range(0, NUMBER_OF_COLUMNS):
            newPosition = self.pos - 8*x
            if newPosition > 0 and not Utils.isCollision(newPosition, allPositions):
                self.possiblePositions.append(newPosition)

        # Horizontal
        currentRow, possiblePositions = Position.get_row_and_possible_places_in_row(self.pos)

        for x in possiblePositions:
            newPosition = x
            if newPosition is not self.pos and not Utils.isCollision(newPosition, allPositions):
                self.possiblePositions.append(newPosition)

    def get_possible_moves(self):
        return self.possiblePositions
