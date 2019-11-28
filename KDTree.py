import statistics


class KDTree():

    class Point:
        def __init__(self, value, left, right):
            self.val = value
            self.left = left
            self.right = right

    def createKDTree(self, points, dimension):
        if len(points) > 1:
            coordinate = [point[dimension] for point in points]
            pivot = statistics.median_low(coordinate)
            less = []
            equal = []
            greater = []
            for point in points:
                if point[dimension] < pivot:
                    less.append(point)
                elif point[dimension] == pivot:
                    equal.append(point)
                elif point[dimension] > pivot:
                    greater.append(point)
            return KDTree.Point(equal[0], self.createKDTree(less+equal[1:], (dimension+1) % 2), self.createKDTree(greater, (dimension+1) % 2))
        elif len(points) == 1:
            return KDTree.Point(points[0], None, None)
        else:
            return None

    def query_range(self, rect2):
        return self.searchForStart(self.tree, rect2.min, rect2.max, 0)

    def searchForStart(self, point, mins, maxs, dimension):
        if point == None:
            return []
        elif point.val[dimension] > maxs[dimension]:
            return self.searchForStart(point.left, mins, maxs, (dimension+1) % 2)
        elif point.val[dimension] < mins[dimension]:
            return self.searchForStart(point.right, mins, maxs, (dimension+1) % 2)
        else:
            return self.checkPoint(point, mins, maxs, (dimension+1) % 2)

    def checkPoint(self, point, mins, maxs, dimension):
        if point.val[dimension] >= mins[dimension] and point.val[dimension] <= maxs[dimension]:
            return [point.val] + self.searchForStart(point.left, mins, maxs, dimension) + self.searchForStart(point.right, mins, maxs, dimension)
        else:
            return self.searchForStart(point.left, mins, maxs, dimension) + self.searchForStart(point.right, mins, maxs, dimension)

    def __init__(self, points):
        self.tree = self.createKDTree(points, 0)
