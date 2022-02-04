import pygame
from cmath import sqrt
import math


class Location:

    def __init__(self, rect):
        self.rect = rect
        self.lastX = 0
        self.lastY = 0

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

        return self

    def direction(self):
        dx = self.X() - self.lastX
        dy = self.Y() - self.lastY
        if dx != 0:
            dx = (dx / abs(dx))
        if dy != 0:
            dy = (dy / abs(dy))

        return (dx, dy)

    def direction(self,location):
        dx = self.X() - location.X()
        dy = self.Y() - location.Y()
        if dx != 0:
            dx = (dx / abs(dx))
        if dy != 0:
            dy = (dy / abs(dy))

        return (dx, dy)

    def add(self, x, y):
        self.set(self.rect.x + x, self.rect.y + y)
        return self

    def multiply(self, factor):
        self.set(self.rect.x * factor, self.rect.y * factor)

    def distance(self, location):
        return math.hypot(self.X() - location.X(), self.Y() - location.Y())

    def clone(self):
        rect = self.rect.copy()
        rect.x = self.rect.x
        rect.y = self.rect.y
        return Location(rect)

    def __str__(self):
        return f"Rect: {self.rect} LastX: {self.lastX}  LastY: {self.lastY}"
