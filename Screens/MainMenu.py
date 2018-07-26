__author__ = 'psheppard16'
from tkinter import *
class MainMenu:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="blue", width=self.parent.width, height=self.parent.height)
        self.f.pack_propagate(0)
        self.startB = Button(self.root, text="Start", command=self.start)
        self.startB.pack(in_=self.f)
        self.optionsB = Button(self.root, text="Options", command=self.options)
        self.optionsB.pack(in_=self.f)
        self.instructionsB = Button(self.root, text="Instructions", command=self.instructions)
        self.instructionsB.pack(in_=self.f)

    def options(self):
        self.window.rMenu = "options"

    def start(self):
        self.window.rMenu = "gameEngine"

    def instructions(self):
        self.window.rMenu = "instructions"

    def hide(self):
        self.f.pack_forget()