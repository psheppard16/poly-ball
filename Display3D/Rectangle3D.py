import Display3D.util3D as util3D
from Display3D.Polygon import *
class Rectangle3D:
    def __init__(self, perspective, location, dimensions, angles, color):
        self.color = color
        self.perspective = perspective
        self.perspective.objectList.append(self)
        self.location = location
        self.dimensions = dimensions
        self.angles = angles

    def getSides(self):
        point1 = util3D.multiAxisRotation(self.getRelPoint(1), self.angles)
        point2 = util3D.multiAxisRotation(self.getRelPoint(2), self.angles)
        point3 = util3D.multiAxisRotation(self.getRelPoint(3), self.angles)
        point4 = util3D.multiAxisRotation(self.getRelPoint(4), self.angles)
        point5 = util3D.multiAxisRotation(self.getRelPoint(5), self.angles)
        point6 = util3D.multiAxisRotation(self.getRelPoint(6), self.angles)
        point7 = util3D.multiAxisRotation(self.getRelPoint(7), self.angles)
        point8 = util3D.multiAxisRotation(self.getRelPoint(8), self.angles)

        point1 = self.addLocation(point1)
        point2 = self.addLocation(point2)
        point3 = self.addLocation(point3)
        point4 = self.addLocation(point4)
        point5 = self.addLocation(point5)
        point6 = self.addLocation(point6)
        point7 = self.addLocation(point7)
        point8 = self.addLocation(point8)

        point1 = util3D.multiAxisRotation(point1, self.perspective.angles)
        point2 = util3D.multiAxisRotation(point2, self.perspective.angles)
        point3 = util3D.multiAxisRotation(point3, self.perspective.angles)
        point4 = util3D.multiAxisRotation(point4, self.perspective.angles)
        point5 = util3D.multiAxisRotation(point5, self.perspective.angles)
        point6 = util3D.multiAxisRotation(point6, self.perspective.angles)
        point7 = util3D.multiAxisRotation(point7, self.perspective.angles)
        point8 = util3D.multiAxisRotation(point8, self.perspective.angles)

        point1 = self.addFocusPoint(point1)
        point2 = self.addFocusPoint(point2)
        point3 = self.addFocusPoint(point3)
        point4 = self.addFocusPoint(point4)
        point5 = self.addFocusPoint(point5)
        point6 = self.addFocusPoint(point6)
        point7 = self.addFocusPoint(point7)
        point8 = self.addFocusPoint(point8)

        side1 = [point1, point2, point3, point4]
        side2 = [point5, point6, point7, point8]
        side3 = [point2, point3, point7, point6]
        side4 = [point1, point4, point8, point5]
        side5 = [point3, point4, point8, point7]
        side6 = [point1, point2, point6, point5]
        sides = [Polygon(side1, self.color), Polygon(side2, self.color), Polygon(side3, self.color),
                 Polygon(side4, self.color), Polygon(side5, self.color), Polygon(side6, self.color)]
        return sides

    def getRelPoint(self, pointNumber):
        if pointNumber == 1:
            return (-self.dimensions[0], -self.dimensions[1], -self.dimensions[2])
        elif pointNumber == 2:
            return (self.dimensions[0], -self.dimensions[1], -self.dimensions[2])
        elif pointNumber == 3:
            return (self.dimensions[0], self.dimensions[1], -self.dimensions[2])
        elif pointNumber == 4:
            return (-self.dimensions[0], self.dimensions[1], -self.dimensions[2])
        elif pointNumber == 5:
            return (-self.dimensions[0], -self.dimensions[1], self.dimensions[2])
        elif pointNumber == 6:
            return (self.dimensions[0], -self.dimensions[1], self.dimensions[2])
        elif pointNumber == 7:
            return (self.dimensions[0], self.dimensions[1], self.dimensions[2])
        elif pointNumber == 8:
            return (-self.dimensions[0], self.dimensions[1], self.dimensions[2])

    def addLocation(self, point):
        x = point[0] - self.perspective.focusLocation[0] + self.location[0]
        y = point[1] - self.perspective.focusLocation[1] + self.location[1]
        z = point[2] - self.perspective.focusLocation[2] + self.location[2]
        return (x, y, z)

    def addFocusPoint(self, point):
        x = point[0] + self.perspective.focusLocation[0]
        y = point[1] + self.perspective.focusLocation[1]
        z = point[2] + self.perspective.focusLocation[2]
        return (x, y, z)

    def setLocation(self, location):
        self.location = location

    def setAngle(self, angles):
        self.angles = angles

    def setDimensions(self, dimensions):
        self.dimensions = dimensions

    def move(self, vector):
        self.location = util3D.add_v3v3(self.location, vector)

    def changeAngle(self, angles):
        self.angles = util3D.add_v3v3(self.angles, angles)


