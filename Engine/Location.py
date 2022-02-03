import pygame
from cmath import sqrt


class Location:

    def __init__(self, rect):
        self.rect = rect
        self.lastX = 0
        self.lastY = 0
        self.directionX = 0
        self.directionY = 0

    def X(self):
        return self.rect.topleft[0]

    def height(self):
        return self.rect.h

    def width(self):
        return self.rect.w

    def Y(self):
        return self.rect.topleft[1]

    def set(self, x, y):
        self.lastX = self.rect.x
        self.lastY = self.rect.y
        self.rect.x = x
        self.rect.y = y
        self.directionX = x - self.lastX
        self.directionY = y - self.lastY
        return self

    def add(self, x, y):
        self.set(self.rect.x + x, self.rect.y + y)
        return self

    def multiply(self, factor):
        self.set(self.rect.x * factor, self.rect.y * factor)

    def distance(self, location):
        p1 = int(self.X() - location.X())
        p2 = int(self.Y() - location.Y())
        return sqrt( (p1 * p1) - (p2 * p2)).real

    def clone(self):
        rect = self.rect.copy()
        rect.x = self.rect.x
        rect.y = self.rect.y
        return Location(rect)

    def __str__(self):
        return f"Rect: {self.rect} LastX: {self.lastX}  LastY: {self.lastY}"
