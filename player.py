from tkinter import *
from math import *



class Player():
    def __init__(self, x=0, y=0, direction=0, speed=5, canvas=Canvas, size=10, center=(100, 100)):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.canvas = canvas
        self.size = size
        self.center = center
        self.vel = 0
    def move(self, direction, speed:int = None):
        if speed == None:
            speed = self.speed
        self.x += cos(radians(direction))*speed
        self.y += sin(radians(direction))*speed

    def draw(self, x=-1, y=-1):
        if x==-1:
            x = self.center[0]
        if y==-1:
            y = self.center[1]
        self.canvas.create_rectangle(x-self.size, y-self.size, x+self.size, y+self.size)