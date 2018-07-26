__author__ = 'psheppard16'
import math
from Display3D.Sphere import *
class Ball:
    def __init__(self, window, perspective):
        self.window = window
        self.perspective = perspective
        self.radius = 100
        self.color = "green"
        self.angles = (0, 0, 0)
        self.location = (0, 300, 0)
        self.lastL = (0, 300, -250)
        self.GRAVITY = 150
        self.AIR_RESISTANCE = .0000000002
        self.FRICTION = 1
        self.ballSphere = Sphere(perspective, self.location, self.radius, self.angles, self.color)

    def run(self):
        if self.location[1] > self.radius:
            self.accelerate((0, -self.GRAVITY * self.window.frameRate.TICK_SPEED, 0))
        xRes = math.pi * self.radius ** 2 * self.getXSpeed() ** 2 * self.AIR_RESISTANCE * self.window.frameRate.TICK_SPEED
        yRes = math.pi * self.radius ** 2 * self.getYSpeed() ** 2 * self.AIR_RESISTANCE * self.window.frameRate.TICK_SPEED
        zRes = math.pi * self.radius ** 2 * self.getZSpeed() ** 2 * self.AIR_RESISTANCE * self.window.frameRate.TICK_SPEED
        self.accelerate((math.copysign(xRes, -self.getXSpeed()), math.copysign(yRes, -self.getYSpeed()), math.copysign(zRes, -self.getZSpeed())))
        self.collisionCheck()
        self.move()
        self.paddleCollision(self.window.gameEngine.paddle1)
        self.paddleCollision(self.window.gameEngine.paddle2)
        self.endCheck()
        self.ballSphere.setLocation(self.location)
        self.updateObject()

    def paddleCollision(self, paddle):
        if math.copysign(1, self.location[2]) == math.copysign(1, paddle.location[2]):
            if abs(self.location[2]) + self.radius > abs(paddle.location[2]) - paddle.dimensions[2]:
                if abs(self.location[2]) < abs(paddle.location[2]) + paddle.dimensions[2]:
                    if math.copysign(1, self.getZSpeed()) == math.copysign(1, self.location[2]):
                        if self.location[1] < paddle.location[1] + paddle.dimensions[1] and self.location[1] > paddle.location[1] - paddle.dimensions[1]:
                            if self.location[0] < paddle.location[0] + paddle.dimensions[0] and self.location[0] > paddle.location[0] - paddle.dimensions[0]:
                                maxAngle = math.pi / 4
                                relativeLocation = paddle.location[0] - self.location[0]
                                paddleRatio = relativeLocation / paddle.dimensions[0]
                                angle = maxAngle * paddleRatio
                                xzSpeed = math.sqrt(self.getXSpeed() ** 2 + self.getZSpeed() ** 2)
                                if angle > 0:
                                    self.setSpeed((xzSpeed * -math.sin(angle), self.getYSpeed(), xzSpeed * -math.copysign(1.1, paddle.location[2]) * math.cos(angle)))
                                else:
                                    self.setSpeed((xzSpeed * -math.sin(angle), self.getYSpeed(), xzSpeed * -math.copysign(1.1, paddle.location[2]) * math.cos(angle)))

    def updateObject(self):
        self.ballSphere.update(self.perspective, self.location, self.radius, self.angles, self.color)

    def endCheck(self):
        if self.location[2] < -500 - self.radius * 2 or self.location[2] > 500 + self.radius * 2:
            self.setPosition((0, 300, 0))
            self.setSpeed((0, 0, -150))

    def move(self):
        calculusAdj = 0
        if (self.getYSpeed() > 0 and self.location[1] > self.radius):
            calculusAdj = (.5 * (self.window.frameRate.TICK_SPEED ** 2) * -self.GRAVITY) # must account for lost displacement due to framerate and gravity
        elif self.location[1] > self.radius:
            calculusAdj = (.5 * (self.window.frameRate.TICK_SPEED ** 2) * self.GRAVITY)
        self.changePosition((self.getXSpeed() * self.window.frameRate.TICK_SPEED,
                             self.getYSpeed() * self.window.frameRate.TICK_SPEED + calculusAdj,
                             self.getZSpeed() * self.window.frameRate.TICK_SPEED))

    def collisionCheck(self):
        if self.location[1] <= self.radius and self.getYSpeed() < 0:
            self.setSpeed((self.getXSpeed() * self.FRICTION,
                          abs(self.getYSpeed()),
                          self.getZSpeed() * self.FRICTION))
        if self.location[0] < -500 + self.radius and self.getXSpeed() < 0:
            self.setSpeed((-self.getXSpeed() * self.FRICTION,
                           self.getYSpeed(),
                           self.getZSpeed() * self.FRICTION))
        if self.location[0] > 500 - self.radius and self.getXSpeed() > 0:
            self.setSpeed((-self.getXSpeed() * self.FRICTION,
                           self.getYSpeed(),
                           self.getZSpeed() * self.FRICTION))

    def setPosition(self, newPosition):
        self.lastL = util3D.add_v3v3(self.location, util3D.mul_v3_fl(self.getVelocity(), -1))
        self.location = newPosition

    def changePosition(self, vector):
        self.location = util3D.add_v3v3(self.location, vector)
        self.lastL = util3D.add_v3v3(self.lastL, vector)

    def changeAngle(self, vector):
        self.angles= util3D.add_v3v3(self.angles, vector)

    def getXSpeed(self):
        return self.location[0] - self.lastL[0]

    def getYSpeed(self):
        return self.location[1] - self.lastL[1]

    def getZSpeed(self):
        return self.location[2] - self.lastL[2]

    def getVelocity(self):
        return (self.getXSpeed(), self.getYSpeed(), self.getZSpeed())

    def getSpeed(self):
        return math.sqrt(self.getXSpeed() ** 2 + self.getYSpeed() ** 2 + self.getZSpeed() ** 2)

    def accelerate(self, forceVector):
        self.lastL = util3D.add_v3v3(self.lastL, util3D.mul_v3_fl(forceVector, -1))

    def setSpeed(self, velocity):
        self.lastL = util3D.add_v3v3(self.location, util3D.mul_v3_fl(velocity, -1))

