from Vec2 import *

class Rect2:
    def __init__(self, a, b):
        self.min = a
        self.max = b

    def center(self):
        return (self.min + self.max) / 2.0

    def width(self):
        return abs(self.max.x - self.min.x)

    def height(self):
        return abs(self.max.y - self.min.y)

    def extent(self):
        return self.max - self.min

    def contains_point(self, p):
        return p.x >= self.min.x and p.x <= self.max.x and p.y >= self.min.y and p.y <= self.max.y

    def contains_rect(self, other):
        return other.min.x >= self.min.x and other.max.x <= self.max.x and other.min.y >= self.min.y and other.max.y <= self.max.y

    def intersects_rect(self, other):
        return self.max.x >= other.min.x and self.max.y >= other.min.y and self.min.x <= other.max.x and self.min.y <= other.max.y

    def __str__(self):
        return f'({self.min}, {self.max})'

    def __repr__(self):
        return f'({self.min}, {self.max})'

def point_set_bounding_box(points):
    minx = float('inf')
    miny = float('inf')
    maxx = float('-inf')
    maxy = float('-inf')

    for x, y in points:
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y

    return Rect2(Vec2(minx, miny), Vec2(maxx, maxy))
