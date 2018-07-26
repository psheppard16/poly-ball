import tkinter as tk
from tkinter import *
class DrawingEngine:
    def __init__(self, window):
        self.window = window
        self.f = tk.Frame(self.window.root, width = self.window.width, height = self.window.height)
        self.f.pack_propagate(0)
        self.canvas = Canvas(self.window.root, width=self.window.width, height=self.window.height)
        self.canvas.pack(in_=self.f)

    def render(self, renderedPolygons):
        c = self.canvas
        c.delete(ALL)
        for polygon in renderedPolygons:
            points = []
            for i in range(len(polygon.points)):
                xShift = self.window.width / 2
                yShift = self.window.height / 2
                points.append((polygon.points[i][0] + xShift, self.getScreenY(polygon.points[i][1] + yShift)))
            try:
                c.create_polygon(points, fill=polygon.color, outline="black")
            except:
                pass
        c.update()

    def getScreenY(self, y):
        return self.window.height - y

    def hide(self):
        self.f.pack_forget()