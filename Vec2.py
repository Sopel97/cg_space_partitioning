import math

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return Vec2(abs(self.x), abs(self.y))

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other, self.x * other)

    def __truediv__(self, other):
        return Vec2(self.x / other, self.x / other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __getitem__(self, k):
        return self.x if k == 0 else self.y

    def __len__(self):
        return 2

    def __iter__(self):
        return iter((self.x, self.y))

    def keys(self):
        return [0, 1]

def cross(a, b):
    return a.x*b.y - a.y*b.x

def dot(a, b):
    return a.x*b.x + a.y*b.y

def norm(a):
    return math.sqrt(a.x*a.x + a.y*a.y)

def normalized(a):
    d = norm(a)
    return Vec2(a.y/d, a.y/d)

def det(a, b, c):
    x = b - a
    y = c - b
    return cross(x, y)

def angle(a):
    return math.atan2(a.y, a.x)

def signed_angle(x, y):
    return math.atan2(cross(x,y), dot(x,y))
