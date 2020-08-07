IMG_LOCATION = "./chessboard/img/"

NUMBER_OF_ROWS = 8
NUMBER_OF_COLUMNS = 8
DIMENSION_OF_EACH_SQUARE = 64
BOARD_COLOR_1 = "#DDB88C"
BOARD_COLOR_2 = "#A66D4F"

WHITE = 0
BLACK = 1

NUMBER_OF_STARTING_PAWNS = 8
NUMBER_OF_STARTING_RKB = 2
NUMBER_OF_STARTING_ROYALS = 1

WHITE_PAWN = {'fileName': "wP.png",
              'startLocations': [49, 50, 51, 52, 53, 54, 55, 56],
              'color': WHITE}
WHITE_ROOKS = {'fileName': "wR.png",
               'startLocations': [57, 64],
               'color': WHITE}
WHITE_KNIGHTS = {'fileName': "wN.png",
                 'startLocations': [58, 63],
                 'color': WHITE}
WHITE_BISHOPS = {'fileName': "wB.png",
                 'startLocations': [59, 62],
                 'color': WHITE}
WHITE_QUEEN = {'fileName': "wQ.png",
               'startLocations': [60],
               'color': WHITE}
WHITE_KING = {'fileName': "wK.png",
              'startLocations': [61],
              'color': WHITE}

BLACK_PAWN = {'fileName': 'bP.png',
              'startLocations': [9, 10, 11, 12, 13, 14, 15, 16],
              'color': BLACK}
BLACK_ROOKS = {'fileName': "bR.png",
               'startLocations': [1, 8],
               'color': BLACK}
BLACK_KNIGHTS = {'fileName': "bN.png",
                 'startLocations': [2, 7],
                 'color': BLACK}
BLACK_BISHOPS = {'fileName': "bB.png",
                 'startLocations': [3, 6],
                 'color': BLACK}
BLACK_QUEEN = {'fileName': "bQ.png",
               'startLocations': [5],
               'color': BLACK}
BLACK_KING = {'fileName': "bK.png",
              'startLocations': [4],
              'color': BLACK}
