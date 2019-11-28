import numpy as np
import math
import time

from Vec2 import *
from Rect2 import *
from QuadTree2 import *

def _rects_for_center_with_area(centers, area):
    half_diagonal = math.sqrt(area)
    half_extent = Vec2(half_diagonal, half_diagonal)
    return [Rect2(center - half_extent, center + half_extent) for center in centers]

def _points1(n):
    '''
    Random points on a square.
    '''
    return [Vec2(x, y) for x, y in np.random.rand(n, 2)]

def _rects1(n, area):
    return _rects_for_center_with_area(_points1(n), area)

def _points2(n):
    '''
    Random points on an axis aligned line.
    '''
    return [Vec2(x, 0.0) for x in np.random.rand(n)]

def _rects2(n, area):
    return _rects_for_center_with_area(_points2(n), area)

def _points3(n):
    '''
    Random points on a not axis aligned aligned line.
    '''
    return [Vec2(x, x) for x in np.random.rand(n)]

def _rects3(n, area):
    return _rects_for_center_with_area(_points3(n), area)

def _points4(n):
    '''
    Random points on a square (non uniform)
    '''
    return [Vec2(x**3, y**3) for x, y in np.random.rand(n, 2)]

def _rects4(n, area):
    return _rects_for_center_with_area(_points4(n), area)

def _points5(n):
    '''
    Random points on a rectangle with high aspect ratio
    '''
    return [Vec2(x*100.0, y) for x, y in np.random.rand(n, 2)]

def _rects5(n, area):
    return _rects_for_center_with_area(_points5(n), area)

def _points6(n):
    '''
    Random points on a circle.
    '''
    return [Vec2(math.cos(theta), math.sin(theta)) for theta in np.random.rand(n) * (math.pi * 2)]

def _rects6(n, area):
    return _rects_for_center_with_area(_points6(n), area)

_point_counts = [10, 100, 1000, 10000, 100000, 1000000]
_rect_areas = [1, 0.1, 0.01, 0.0001, 0.000001]
_dataset_generators = [
    (_points1, _rects1, "set_1"),
    (_points2, _rects2, "set_2"),
    (_points3, _rects3, "set_3"),
    (_points4, _rects4, "set_4"),
    (_points5, _rects5, "set_5"),
    (_points6, _rects6, "set_6")
]

def _bench_case(cls, name, points, rects):
    tree = cls(points)

    start = time.time()

    total_points_found = 0
    for rect in rects:
        total_points_found += len(tree.query_range(rect))

    end = time.time()
    return (end - start) / len(rects), total_points_found // len(rects)

def bench(cls, num_queries):
    name = cls.__name__
    print('Data structure name\tDataset name\tPoint count\tRect area\tSingle query time\tAvg. points found')
    for point_generator, rect_generator, set_name in _dataset_generators:
        for point_count in _point_counts:
            points = point_generator(point_count)
            for rect_area in _rect_areas:
                rects = rect_generator(num_queries, rect_area)

                seconds_per_query, avg_points_found = _bench_case(cls, name, points, rects)
                print(f'{name}\t{set_name}\t{point_count}\t{rect_area}\t{seconds_per_query}\t{avg_points_found}')


if __name__ == '__main__':
    bench(QuadTree2, 16)
