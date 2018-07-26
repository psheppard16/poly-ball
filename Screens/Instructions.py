from tkinter import *
class Instructions:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="blue", width=self.window.width, height =self.window.width)
        self.f.pack_propagate(0)
        self.cancel = Button(self.root, text="Cancel", command=self.cancel)
        self.cancel.pack(in_=self.f)

    def cancel(self):
        self.window.rMenu = "mainMenu"

    def hide(self):
        self.f.pack_forget()