import tkinter as tk

from chessboard import model
from chessboard.view import View
from chessboard.game.coordinates.position import Position
from .configuration import *


class Controller():

    def __init__(self):
        self.root = tk.Tk()
        self.model = model.Model()
        self.view=View(self.root, self, self.model.game.whiteTeam, self.model.game.blackTeam)
        self.currentMovePiece = None
        self.firstPress = False
        self.move = WHITE

    def hello_world_button(self, event):
        #reset
        pass

    def board_press(self, event):
        if self.firstPress is False:
            self.firstPress = True
            hasPiece, self.currentMovePiece = self.model.game.has_piece_on(Position.get_location(event.x, event.y))
            if hasPiece:
                if self.currentMovePiece.color != self.move:
                    self.currentMovePiece = None
                    pass
        else:
            pass
            # move piece

    def place_piece(self, event):
        self.firstPress = False
        position = Position.get_location(event.x, event.y)
        if self.currentMovePiece is not None:
            possibleMoves = self.currentMovePiece.get_possible_moves()
            isMovePossible = False

            for pos in possibleMoves:
                if position == pos:
                    isMovePossible = True
                    break

            if isMovePossible:
                self.currentMovePiece.set_position(position)
                if self.move == WHITE:
                    self.move = BLACK
                else:
                    self.move = WHITE

            print("new position: ", position)
        self.view.refresh()
        self.model.refresh()

    def run(self):
        self.root.title("Chess board v0.0.1")
        self.root.deiconify()
        self.root.mainloop()
        pass
