from Vec2 import *
from Rect2 import *
from QuadTree2 import *

import numpy as np

print(Vec2(1.0, 2.0))


points = [Vec2(x, y) for x,y in np.random.rand(100, 2)]
rect0 = Rect2(Vec2(0.0, 0.0), Vec2(1.0, 1.0))
rect1 = Rect2(Vec2(0.0, 0.0), Vec2(1.0, 1.0)/2)
rect2 = Rect2(Vec2(0.0, 0.0), Vec2(1.0, 1.0)/4)
rect3 = Rect2(Vec2(0.0, 0.0), Vec2(1.0, 1.0)/8)
qt = QuadTree2(points)
print(len(qt.query_range(rect0)))
print(len(qt.query_range(rect1)))
print(len(qt.query_range(rect2)))
print(len(qt.query_range(rect3)))