#!/usr/bin/python3

import tkinter
import tkinter.ttk as ttk
import game_model

class MainWindow(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self._theme = {"BG": "#000"}
        self.parent = parent
        self.init_GUI()

    def init_GUI(self):
        
        self.parent.title("PacPerson")
        # This just makes the Tkinter windows look and behave a little more
        # like a modern OS than the default style
        self.style = ttk.Style()
        self.style.theme_use("default")

        frame = ttk.Frame(self, relief=tkinter.RAISED, borderwidth=1)
        frame.pack(side=tkinter.LEFT, fill=tkinter.BOTH, anchor=tkinter.W, expand=True)

        self._canvas = tkinter.Canvas(frame, background=self._theme["BG"])
        self._canvas.pack(fill=tkinter.BOTH, expand=1)

        self.pack(fill=tkinter.BOTH, expand=True)
        
        self._newGame = tkinter.Button(self, text="New")
        self._quitGame = tkinter.Button(self, text="Quit")
        self._newGame.pack(side=tkinter.BOTTOM, padx=5, pady=5)
        self._quitGame.pack(side=tkinter.BOTTOM, padx=5, pady=5)
        

    def draw(self, game_board):
        for entity in game_board:
            self.draw_entity(entity)
            
    def process_input(self):
        pass

    def draw_entity(self, entity):
        pass

    def update(self, game_board):
        pass

