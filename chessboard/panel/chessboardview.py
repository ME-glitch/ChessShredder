import tkinter as tk
from tkinter import *
from ..configuration import *
from chessboard.game.coordinates.position import Position


class ChessBoardView:

    def __init__(self, master, whiteTeam, blackTeam):
        self.master = master
        self.whiteTeam = whiteTeam
        self.blackTeam = blackTeam
        self.w = DIMENSION_OF_EACH_SQUARE * NUMBER_OF_ROWS
        self.h = DIMENSION_OF_EACH_SQUARE * NUMBER_OF_COLUMNS
        self.chess_board_canvas = Canvas(self.master, width=self.w, height=self.h)
        self.chess_board_canvas.pack(side=LEFT, fill=tk.BOTH, expand=YES)
        self.create_board()

    def get_canvas(self):
        return self.chess_board_canvas

    def refresh(self):
        self.create_board()

    def create_board(self):
        self.create_rows()
        self.create_columns()
        self.fill_board()
        self.populate_board_with_pieces()

    def create_rows(self):
        for x in range(1, NUMBER_OF_ROWS + 1):
            self.chess_board_canvas.create_line(0, x * DIMENSION_OF_EACH_SQUARE, self.w, x * DIMENSION_OF_EACH_SQUARE,
                                                fill="black")

    def create_columns(self):
        for y in range(1, NUMBER_OF_COLUMNS + 1):
            self.chess_board_canvas.create_line(y * DIMENSION_OF_EACH_SQUARE, 0, y * DIMENSION_OF_EACH_SQUARE, self.h,
                                                fill="black")

    def fill_board(self):
        self.fill_board_black()
        self.fill_board_white()

    def fill_board_black(self):
        for x in range(0, int(NUMBER_OF_ROWS / 2)):
            for y in range(0, int(NUMBER_OF_COLUMNS / 2)):
                x0 = x * DIMENSION_OF_EACH_SQUARE * 2 + DIMENSION_OF_EACH_SQUARE
                y0 = y * DIMENSION_OF_EACH_SQUARE * 2
                x1 = x0 + DIMENSION_OF_EACH_SQUARE
                y1 = y0 + DIMENSION_OF_EACH_SQUARE
                self.chess_board_canvas.create_rectangle(x0, y0, x1, y1, fill=BOARD_COLOR_2)

        for x in range(0, int(NUMBER_OF_ROWS / 2)):
            for y in range(0, int(NUMBER_OF_COLUMNS / 2)):
                x0 = x * DIMENSION_OF_EACH_SQUARE * 2
                y0 = y * DIMENSION_OF_EACH_SQUARE * 2 + DIMENSION_OF_EACH_SQUARE
                x1 = x0 + DIMENSION_OF_EACH_SQUARE
                y1 = y0 + DIMENSION_OF_EACH_SQUARE
                self.chess_board_canvas.create_rectangle(x0, y0, x1, y1, fill=BOARD_COLOR_2)

    def fill_board_white(self):
        for x in range(0, int(NUMBER_OF_ROWS / 2)):
            for y in range(0, int(NUMBER_OF_COLUMNS / 2)):
                x0 = x * DIMENSION_OF_EACH_SQUARE * 2
                y0 = y * DIMENSION_OF_EACH_SQUARE * 2
                x1 = x0 + DIMENSION_OF_EACH_SQUARE
                y1 = y0 + DIMENSION_OF_EACH_SQUARE
                self.chess_board_canvas.create_rectangle(x0, y0, x1, y1, fill=BOARD_COLOR_1)

        for x in range(0, int(NUMBER_OF_ROWS / 2)):
            for y in range(0, int(NUMBER_OF_COLUMNS / 2)):
                x0 = x * DIMENSION_OF_EACH_SQUARE * 2 + DIMENSION_OF_EACH_SQUARE
                y0 = y * DIMENSION_OF_EACH_SQUARE * 2 + DIMENSION_OF_EACH_SQUARE
                x1 = x0 + DIMENSION_OF_EACH_SQUARE
                y1 = y0 + DIMENSION_OF_EACH_SQUARE
                self.chess_board_canvas.create_rectangle(x0, y0, x1, y1, fill=BOARD_COLOR_1)

    def populate_board_with_pieces(self):
        self.place_white_pieces()
        self.place_black_pieces()

    def place_white_pieces(self):
        self.place_white_rooks()
        self.place_white_knights()
        self.place_white_bishops()
        self.place_white_royals()
        self.place_white_pawns()

    def place_white_rooks(self):
        for x in range(0, len(self.whiteTeam.player.rooks)):
            x0, y0 = Position.get_position(self.whiteTeam.player.rooks[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.whiteTeam.player.rooks[x].get_photo(),
                                                 anchor=NW)

    def place_white_knights(self):
        for x in range(0, len(self.whiteTeam.player.knights)):
            x0, y0 = Position.get_position(self.whiteTeam.player.knights[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.whiteTeam.player.knights[x].get_photo(),
                                                 anchor=NW)

    def place_white_bishops(self):
        for x in range(0, len(self.whiteTeam.player.bishops)):
            x0, y0 = Position.get_position(self.whiteTeam.player.bishops[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.whiteTeam.player.bishops[x].get_photo(),
                                                 anchor=NW)

    def place_white_royals(self):
        xKing, yKing = Position.get_position(self.whiteTeam.player.king[0].get_position())
        self.chess_board_canvas.create_image(xKing,
                                             yKing,
                                             image=self.whiteTeam.player.king[0].get_photo(),
                                             anchor=NW)
        for x in range(0, len(self.whiteTeam.player.queens)):
            x0, y0 = Position.get_position(self.whiteTeam.player.queens[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.whiteTeam.player.queens[x].get_photo(),
                                                 anchor=NW)

    def place_white_pawns(self):
        for x in range(0, len(self.whiteTeam.player.pawns)):
            x0, y0 = Position.get_position(self.whiteTeam.player.pawns[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.whiteTeam.player.pawns[x].get_photo(),
                                                 anchor=NW)

    def place_black_pieces(self):
        self.place_black_rooks()
        self.place_black_knights()
        self.place_black_bishops()
        self.place_black_royals()
        self.place_black_pawns()

    def place_black_rooks(self):
        for x in range(0, len(self.blackTeam.player.rooks)):
            x0, y0 = Position.get_position(self.blackTeam.player.rooks[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.blackTeam.player.rooks[x].get_photo(),
                                                 anchor=NW)

    def place_black_knights(self):
        for x in range(0, len(self.blackTeam.player.knights)):
            x0, y0 = Position.get_position(self.blackTeam.player.knights[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.blackTeam.player.knights[x].get_photo(),
                                                 anchor=NW)

    def place_black_bishops(self):
        for x in range(0, len(self.blackTeam.player.bishops)):
            x0, y0 = Position.get_position(self.blackTeam.player.bishops[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.blackTeam.player.bishops[x].get_photo(),
                                                 anchor=NW)

    def place_black_royals(self):
        xKing, yKing = Position.get_position(self.blackTeam.player.king[0].get_position())
        self.chess_board_canvas.create_image(xKing,
                                             yKing,
                                             image=self.blackTeam.player.king[0].get_photo(),
                                             anchor=NW)

        for x in range(0, len(self.blackTeam.player.queens)):
            x0, y0 = Position.get_position(self.blackTeam.player.queens[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.blackTeam.player.queens[x].get_photo(),
                                                 anchor=NW)

    def place_black_pawns(self):
        for x in range(0, len(self.blackTeam.player.pawns)):
            x0, y0 = Position.get_position(self.blackTeam.player.pawns[x].get_position())
            self.chess_board_canvas.create_image(x0,
                                                 y0,
                                                 image=self.blackTeam.player.pawns[x].get_photo(),
                                                 anchor=NW)
