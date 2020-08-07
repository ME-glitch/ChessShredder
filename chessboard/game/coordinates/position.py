import math

from chessboard.configuration import *


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Position is described by 1..64
    #  |01|02|03|04|05|06|07|08|
    #  |09|10|11|12|13|14|15|16|
    #  |17|18|19|20|21|22|23|24|
    #  |25|26|27|28|29|30|31|32|
    #  |33|34|35|36|37|38|39|40|
    #  |41|42|43|44|45|46|47|48|
    #  |49|50|51|52|53|54|55|56|
    #  |57|58|59|60|61|62|63|64|
    # TODO: Make this nicer
    # TODO: Rename to game position or so
    @staticmethod
    def get_position(pos):
        xCord = ((pos - 1) % 8) * DIMENSION_OF_EACH_SQUARE
        if pos < 9:
            yCord = 0
        elif pos < 17:
            yCord = DIMENSION_OF_EACH_SQUARE
        elif pos < 25:
            yCord = 2 * DIMENSION_OF_EACH_SQUARE
        elif pos < 33:
            yCord = 3 * DIMENSION_OF_EACH_SQUARE
        elif pos < 41:
            yCord = 4 * DIMENSION_OF_EACH_SQUARE
        elif pos < 49:
            yCord = 5 * DIMENSION_OF_EACH_SQUARE
        elif pos < 57:
            yCord = 6 * DIMENSION_OF_EACH_SQUARE
        else:
            yCord = 7 * DIMENSION_OF_EACH_SQUARE

        return xCord, yCord

    @staticmethod
    def get_location(x,y):
        posX = math.floor((x / DIMENSION_OF_EACH_SQUARE) % 8+1)
        posY = math.floor((y / DIMENSION_OF_EACH_SQUARE) % 8)
        position = posX+posY*8
        return position

    @staticmethod
    # TODO do this smarter
    def get_row_and_possible_places_in_row(pos):
        if pos < 9:
            return 1, [1, 2, 3, 4, 5, 6, 7, 8]
        elif pos < 17:
            return 2, [9, 10, 11, 12, 13, 14, 15, 16]
        elif pos < 25:
            return 3, [17, 18, 19, 20, 21, 22, 23, 24]
        elif pos < 33:
            return 4, [25, 26, 27, 28, 29, 30, 31, 32]
        elif pos < 41:
            return 5, [33, 34, 35, 36, 37, 38, 39, 40]
        elif pos < 49:
            return 6, [41, 42, 43, 44, 45, 46, 47, 48]
        elif pos < 57:
            return 7, [49, 50, 51, 52, 53, 54, 55, 56]
        elif pos < 65:
            return 8, [57, 58, 59, 60, 61, 62, 63, 64]

    @staticmethod
    def get_row_positions(pos):
        print()
        pass

