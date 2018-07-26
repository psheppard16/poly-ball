from Display3D.Perspective import *
from Game.Paddle import *
from Game.Ball import *
class GameEngine:
    def __init__(self, window):
        self.window = window
        self.FREE_CAMERA = False
        if self.FREE_CAMERA:
            self.mouseDown = False
            self.mouseStartPoint = (0, 0)
            self.rotation = False
            self.translation = False
            self.distance = 1000
            self.angleXP = 0
            self.angleYP = 0
            self.angleZP = 0
            self.perspectiveX = 0
            self.perspectiveY = 0
            self.perspective = Perspective((self.perspectiveX, self.perspectiveY, 0), self.distance, (math.radians(self.angleXP), math.radians(self.angleYP), math.radians(self.angleZP)))
        else:
            self.perspective = Perspective((0, 0, 0), 1000, (math.radians(0), math.radians(0), math.radians(0)))
        self.paddle2 = Paddle(self.window, self.perspective, -500)
        self.paddle1 = Paddle(self.window, self.perspective, 500)
        self.ball = Ball(self.window, self.perspective)
        self.floor = Rectangle3D(self.perspective, (-465, 0, -500), (1000, 15, 500), (0, 0, 0), "blue")
        self.floor = Rectangle3D(self.perspective, (-465, 0, 500), (1000, 15, 500), (0, 0, 0), "red")

    def runGame(self):
        self.paddle1.run()
        self.paddle2.run()
        self.ball.run()
        if self.FREE_CAMERA:
            if self.mouseDown:
                if self.rotation:
                    x = self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()
                    y = self.window.root.winfo_pointery() - self.window.root.winfo_rooty()
                    xChange = x - self.mouseStartPoint[0]
                    yChange = y - self.mouseStartPoint[1]
                    self.mouseStartPoint = (x, y)
                    self.angleXP -= yChange / 2
                    self.angleYP -= xChange / 2
                elif self.translation:
                    x = self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()
                    y = self.window.root.winfo_pointery() - self.window.root.winfo_rooty()
                    xChange = x - self.mouseStartPoint[0]
                    yChange = y - self.mouseStartPoint[1]
                    self.mouseStartPoint = (x, y)
                    self.perspectiveX -= xChange
                    self.perspectiveY += yChange
            self.perspective.setFocusLocation((self.perspectiveX, self.perspectiveY, 0))
            self.perspective.setDistance(self.distance)
            self.perspective.setAngle((math.radians(self.angleXP), math.radians(self.angleYP), math.radians(self.angleZP)))
            self.perspective.update()
        else:
            self.perspective.setFocusLocation(self.ball.location)
            self.perspective.setAngle((math.radians(-90), math.radians(45), math.radians(90)))
            self.perspective.setDistance(1500)
            self.perspective.update()


    def keyPressed(self, event):
        if self.FREE_CAMERA:
            if event.char == 'r' or event.char == 'R':
                self.rotation = True
            elif event.char == 't' or event.char == 'T':
                self.translation = True
            elif event.keysym == 'Left':
                self.angleZP -= 5
            elif event.keysym == 'Right':
                self.angleZP += 5
        if event.char == 'w' or event.char == 'W':
            self.paddle1.upMove = True
        if event.char == 'a' or event.char == 'A':
            self.paddle1.leftMove = True
        if event.char == 's' or event.char == 'S':
            self.paddle1.downMove = True
        if event.char == 'd' or event.char == 'D':
            self.paddle1.rightMove = True
        if event.keysym == 'Up':
            self.paddle2.upMove = True
        if event.keysym == 'Left':
            self.paddle2.leftMove = True
        if event.keysym == 'Down':
            self.paddle2.downMove = True
        if event.keysym == 'Right':
            self.paddle2.rightMove = True

    def keyReleased(self, event):
        if self.FREE_CAMERA:
            if event.char == 'r' or event.char == 'R':
                self.rotation = False
            elif event.char == 't' or event.char == 'T':
                self.translation = False
        if event.char == 'w' or event.char == 'W':
            self.paddle1.upMove = False
        if event.char == 'a' or event.char == 'A':
            self.paddle1.leftMove = False
        if event.char == 's' or event.char == 'S':
            self.paddle1.downMove = False
        if event.char == 'd' or event.char == 'D':
            self.paddle1.rightMove = False
        if event.keysym == 'Up':
            self.paddle2.upMove = False
        if event.keysym == 'Left':
            self.paddle2.leftMove = False
        if event.keysym == 'Down':
            self.paddle2.downMove = False
        if event.keysym == 'Right':
            self.paddle2.rightMove = False

    def mousePressed(self, event):
        if self.FREE_CAMERA:
            self.mouseDown = True
            self.mouseStartPoint = (event.x, event.y)

    def mouseReleased(self, event):
        if self.FREE_CAMERA:
            self.mouseDown = False