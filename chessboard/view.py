import tkinter as tk
from tkinter import *

from chessboard.panel.chessboardview import ChessBoardView


class View:

    def __init__(self, master, _controller, whiteTeam, blackTeam):
        self.master = master
        self.frame = tk.Frame(master)
        self.controller = _controller
        self.whiteTeam = whiteTeam
        self.blackTeam = blackTeam
        self.top_menu()
        self.create_chess_base()
        # self.canvas.bind binding a mouse click

    def create_chess_base(self):
        self.chessBoardView = ChessBoardView(self.master, self.whiteTeam, self.blackTeam)
        self.chessCanvas = self.chessBoardView.get_canvas()
        self.chessCanvas.bind("<B1-Motion>", self.controller.board_press)
        self.chessCanvas.bind("<ButtonRelease-1>", self.controller.place_piece)
        # create top menu
        # create canvas
        # draw board
        # create bottom frame
        pass

    def refresh(self):
        self.chessCanvas.delete("all")
        self.chessBoardView.refresh()
        self.chessCanvas = self.chessBoardView.get_canvas()

    def top_menu(self):
        self.top_menu_frame = tk.Frame(self.master)
        self.top_menu_frame.pack(side=TOP, fill=tk.BOTH, expand=1)
        self.testButton = tk.Button(self.top_menu_frame, text="Hello World")
        self.testButton.pack(side="top", fill=tk.BOTH)
        self.testButton.bind("<Button>", self.controller.hello_world_button)
