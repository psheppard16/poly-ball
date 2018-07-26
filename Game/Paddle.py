__author__ = 'psheppard16'
from Display3D.Rectangle3D import *
class Paddle:
    def __init__(self, window, perspective, zLocation):
        self.window = window
        self.radius = 100
        self.color = "red"
        self.spawnSweep = 1.0
        self.angles = (0, 0, 0)
        self.dimensions = (350, 125, 25)
        self.location = (0, self.dimensions[1], zLocation)
        self.leftMove = False
        self.rightMove = False
        self.upMove = False
        self.downMove = False
        if self.location[2] > 0:
            self.paddleRect = Rectangle3D(perspective, self.location, self.dimensions, (0, 0, 0), "blue")
        else:
            self.paddleRect = Rectangle3D(perspective, self.location, self.dimensions, (0, 0, 0), "red")


    def run(self):
        self.collisionCheck()
        self.move()
        self.paddleRect.setLocation(self.location)

    def move(self):
        if self.rightMove:
            self.location = util3D.add_v3v3(self.location, (25, 0, 0))
        if self.leftMove:
            self.location = util3D.add_v3v3(self.location, (-25, 0, 0))
        if self.upMove:
            self.location = util3D.add_v3v3(self.location, (0, 25, 0))
        if self.downMove:
            self.location = util3D.add_v3v3(self.location, (0, -25, 0))

    def collisionCheck(self):
        if self.location[0] < -500 + self.dimensions[0]:
            self.leftMove = False
        if self.location[0] > 500 - self.dimensions[0]:
            self.rightMove = False
        if self.location[1] < 0 + self.dimensions[1]:
            self.downMove = False
        if self.location[1] > 500 - self.dimensions[1]:
            self.upMove = False