from Display3D.Polygon import *
import Display3D.util3D as util3D
class RenderFrame:
    def __init__(self, perspective, location, normalVector):
        self.perspective = perspective
        self.location = location
        self.normalVector = normalVector

    def renderPolygons(self, objectList):
        polygonList = self.getPolygons(objectList)
        orderedPolygons = self.orderPolygons(polygonList)
        renderedPolygons = self.mapPolygons(orderedPolygons)
        return renderedPolygons

    def mapPolygons(self, orderedPolygons):
        renderedPolygons = []
        for polygon in orderedPolygons:
            renderedPolygon = Polygon([], polygon.color)
            sideIsInFrame = True
            for point in polygon.points:
                if self.perspective.isInFrame(point):
                    intersectionPoint = util3D.intersectsPlane(self.perspective.location, point, self.location, self.normalVector)
                    if intersectionPoint != None:
                        renderedPolygon.points.append((intersectionPoint[0] - self.perspective.focusLocation[0], intersectionPoint[1] - self.perspective.focusLocation[1], intersectionPoint[2] - self.perspective.focusLocation[2]))
                else:
                    sideIsInFrame = False
            if sideIsInFrame:
                renderedPolygons.append(renderedPolygon)
        return renderedPolygons

    def orderPolygons(self, polygonList):
        orderedPolygon = []
        polygonsToCheck = len(polygonList)
        for i in range(polygonsToCheck):
            largestDistance = 0
            farthestPolygon = ()
            for polygon in polygonList:
                centerPoint = util3D.getCenterOfPoly(polygon.points)
                farthestDistanceToSide = util3D.getFarthestDistance(polygon, self.perspective.location)
                distanceToSide = util3D.getDistance(centerPoint, self.perspective.location)
                average = (farthestDistanceToSide * 0 + distanceToSide)
                if abs(average) > largestDistance:
                    largestDistance = distanceToSide
                    farthestPolygon = polygon
            orderedPolygon.append(farthestPolygon)
            try:
                polygonList.remove(farthestPolygon)
            except:
                pass
        return orderedPolygon

    def getPolygons(self, objectList):
        polygonList = []
        for object in objectList:
            objectPolygons = object.getSides()
            for polygon in objectPolygons:
                polygonList.append(polygon)
        return polygonList



