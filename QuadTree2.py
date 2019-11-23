from Vec2 import *
from Rect2 import *

def subdivide_rect(rect):
    center = rect.center()
    north_west = Rect2(Vec2(rect.min.x, center.y), Vec2(center.x, rect.max.y))
    north_east = Rect2(center, rect.max)
    south_west = Rect2(rect.min, center)
    south_east = Rect2(Vec2(center.x, rect.min.y), Vec2(rect.max.x, center.y))
    return (north_west, north_east, south_west, south_east)

def partition_points_to_subdivisions(rect, points):
    center = rect.center()
    north_west = []
    north_east = []
    south_west = []
    south_east = []

    for p in points:
        if p.x < center.x:
            if p.y < center.y:
                south_west.append(p)
            else:
                north_west.append(p)
        else:
            if p.y < center.y:
                south_east.append(p)
            else:
                north_east.append(p)

    return (north_west, north_east, south_west, south_east)

class QuadTree2:
    class Node:
        def __init__(self, depth, bounds, points, bucket_size, max_depth):
            self.depth = depth
            self.bucket_size = bucket_size
            self.max_depth = max_depth
            self.bounds = bounds

            self.north_west = None
            self.north_east = None
            self.south_west = None
            self.south_east = None

            self.points = points

            if len(self.points) > bucket_size and depth < max_depth:
                self._subdivide()

        def _subdivide(self):
            north_west_b, north_east_b, south_west_b, south_east_b = subdivide_rect(self.bounds)
            north_west_p, north_east_p, south_west_p, south_east_p = partition_points_to_subdivisions(self.bounds, self.points)

            self.north_west = QuadTree2.Node(self.depth + 1, north_west_b, north_west_p, self.bucket_size, self.max_depth)
            self.north_east = QuadTree2.Node(self.depth + 1, north_east_b, north_east_p, self.bucket_size, self.max_depth)
            self.south_west = QuadTree2.Node(self.depth + 1, south_west_b, south_west_p, self.bucket_size, self.max_depth)
            self.south_east = QuadTree2.Node(self.depth + 1, south_east_b, south_east_p, self.bucket_size, self.max_depth)

            self.points = None

        def query_range(self, rect):
            if self.points is not None:
                if self.bounds.contains_rect(rect):
                    return self.points
                else:
                    return [p for p in self.points if rect.contains_point(p)]
            else:
                return \
                    self.north_west.query_range(rect) + \
                    self.north_east.query_range(rect) + \
                    self.south_west.query_range(rect) + \
                    self.south_east.query_range(rect)

        def print(self):
            if self.points is not None:
                print(self.depth, self.points)
            else:
                self.north_west.print()
                self.north_east.print()
                self.south_west.print()
                self.south_east.print()


    def __init__(self, points, bucket_size=10, max_depth=10):
        self.bucket_size = bucket_size
        self.max_depth = max_depth
        self.root = QuadTree2.Node(0, point_set_bounding_box(points), points, bucket_size, max_depth)

    def query_range(self, rect):
        return self.root.query_range(rect)

    def print(self):
        self.root.print();
