from Display3D.RenderFrame import *
from Display3D.Rectangle3D import *
from Display3D.Pyramid3D import *
import math
class Perspective:
    def __init__(self, focusLocation, distance, angles):
        self.objectList = []
        self.angles = angles
        self.distance = distance
        self.focusLocation = focusLocation
        self.location = (focusLocation[0], focusLocation[1], focusLocation[2] + self.distance)
        self.renderFrame = RenderFrame(self, (focusLocation[0], focusLocation[1], focusLocation[2] + self.distance - 1000), (0, 0, 1))
        focusSize = 2.5
        #self.rectangle3D1 = Rectangle3D(self, (self.focusLocation[0] + focusSize * 11, self.focusLocation[1] + 0, self.focusLocation[2] + 0), (focusSize * 6, focusSize, focusSize), (0, 0, 0), "red")
        #self.pyramid3D1 = Pyramid3D(self, (self.focusLocation[0] + focusSize * 22, self.focusLocation[1] + 0, self.focusLocation[2] + 0), (focusSize * 2, focusSize * 2, focusSize * 2), (0, 0, math.pi / 2), "red")
        #self.rectangle3D2 = Rectangle3D(self, (self.focusLocation[0] + 0, self.focusLocation[1] + focusSize * 11, self.focusLocation[2] + 0), (focusSize, focusSize * 6, focusSize), (0, 0, 0), "blue")
        #self.pyramid3D2 = Pyramid3D(self, (self.focusLocation[0] + 0, self.focusLocation[1] + focusSize * 22, self.focusLocation[2] + 0), (focusSize * 2, focusSize * 2, focusSize * 2), (0, 0, 0), "blue")
        #self.rectangle3D3 = Rectangle3D(self, (self.focusLocation[0] + 0, self.focusLocation[1] + 0, self.focusLocation[2] + focusSize * 11), (focusSize, focusSize, focusSize * 6), (0, 0, 0), "green")
        #self.pyramid3D3 = Pyramid3D(self, (self.focusLocation[0] + 0, self.focusLocation[1] + 0, self.focusLocation[2] + focusSize * 22), (focusSize * 2, focusSize * 2, focusSize * 2), (-math.pi / 2, 0, 0), "green")
        #self.rectangle3D4 = Rectangle3D(self, (self.focusLocation[0] + 0, self.focusLocation[1] + 0, self.focusLocation[2] + 0), (focusSize, focusSize, focusSize), (0, 0, 0), "black")

    def update(self):
        self.location = (self.focusLocation[0], self.focusLocation[1], self.focusLocation[2] + self.distance)
        self.renderFrame = RenderFrame(self, (self.focusLocation[0], self.focusLocation[1], self.focusLocation[2] + self.distance - 1000), (0, 0, 1))
        focusSize = 2.5
        #self.rectangle3D1.setLocation((self.focusLocation[0] + focusSize * 11, self.focusLocation[1] + 0, self.focusLocation[2] + 0))
        #self.pyramid3D1.setLocation((self.focusLocation[0] + focusSize * 22, self.focusLocation[1] + 0, self.focusLocation[2] + 0))
        #self.rectangle3D2.setLocation((self.focusLocation[0] + 0, self.focusLocation[1] + focusSize * 11, self.focusLocation[2] + 0))
        #self.pyramid3D2.setLocation((self.focusLocation[0] + 0, self.focusLocation[1] + focusSize * 22, self.focusLocation[2] + 0))
        #self.rectangle3D3.setLocation((self.focusLocation[0] + 0, self.focusLocation[1] + 0, self.focusLocation[2] + focusSize * 11))
        #self.pyramid3D3.setLocation((self.focusLocation[0] + 0, self.focusLocation[1] + 0, self.focusLocation[2] + focusSize * 22))
        #self.rectangle3D4.setLocation((self.focusLocation[0] + 0, self.focusLocation[1] + 0, self.focusLocation[2] + 0))

    def isInFrame(self, point):
        if point[2] <= self.location[2]:
            return True
        else:
            return False

    def setFocusLocation(self, location):
        self.focusLocation = location

    def setAngle(self, angles):
        self.angles = angles

    def setDistance(self, distance):
        self.distance = distance

    def move(self, vector):
        self.location = util3D.add_v3v3(self.location, vector)
        self.focusLocation = util3D.add_v3v3(self.location, (0, 0, -self.distance))

    def changeAngle(self, angles):
        self.angles = util3D.add_v3v3(self.angles, angles)

    def changeDistance(self, change):
        self.distance += change
        self.location = (self.focusLocation[0], self.focusLocation[1], self.focusLocation[2] + self.distance)