from tkinter import *
class Options:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="blue", width=self.window.width, height =self.window.width)
        self.f.pack_propagate(0)

        self.widthLabel = Label(self.root, text="Board Width")
        self.widthLabel.pack(in_=self.f)
        self.width = Spinbox(self.root, from_=1, to=1000)
        self.width.delete(0,"end")
        #self.width.insert(0, self.window.gameEngine.mazeWidth)
        self.width.pack(in_=self.f)

        self.heightLabel = Label(self.root, text="Board Height")
        self.heightLabel.pack(in_=self.f)
        self.height = Spinbox(self.root, from_=1, to=1000)
        self.height.delete(0,"end")
        #self.height.insert(0, self.window.gameEngine.mazeHeight)
        self.height.pack(in_=self.f)

        self.resolution = StringVar()
        self.resolution.set("1280x720")
        self.resolutionM = OptionMenu(self.root, self.resolution, "1280x720", "1366x768", "1600x900", "1920x1080", "2048x1152", "2560x1440")
        self.resolutionM.pack(in_=self.f)
        self.accept = Button(self.root, text="Accept", command=self.accept)
        self.accept.pack(in_=self.f)

    def accept(self):
        #self.window.mazeHeight = int(float(self.height.get()) + 1)
        #self.window.mazeWidth = int(float(self.width.get()) + 1)
        #self.window.requestedScale = float(self.scale.get())
        self.window.rMenu = "mainMenu"

    def hide(self):
        self.f.pack_forget()
