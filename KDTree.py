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
            return KDTree.Point(equal[0], self.createKDTree(less+equal[1:], (dimension+1)%2), self.createKDTree(greater, (dimension+1)%2))
        else:
            return None   
        
    def query_range(self, p1, p2):
        mins = [min(p1[0], p2[0]), min(p1[1], p2[1])]
        maxs = [max(p1[0], p2[0]), max(p1[1], p2[1])]
        
        return self.searchForStart(self.tree, mins, maxs, 0)
        
    def searchForStart(self, point, mins, maxs, dimension):
        if point == None:
            return 0
        elif point.val[dimension] > maxs[dimension]:
            return self.searchForStart(point.left, mins, maxs, (dimension+1)%2)
        elif point.val[dimension] < mins[dimension]:
            return self.searchForStart(point.right, mins, maxs, (dimension+1)%2)
        else:
            return self.checkPoint(point, mins, maxs, (dimension+1)%2)
        
    def checkPoint(self, point, mins, maxs, dimension):
        if point.val[dimension] >= mins[dimension] and point.val[dimension] <= maxs[dimension]:
                return 1 + self.searchForStart(point.left, mins, maxs, (dimension+1)%2) \
                    + self.searchForStart(point.right, mins, maxs, (dimension+1)%2)
        else:
            0 + self.searchForStart(point.left, mins, maxs, (dimension+1)%2) \
                    + self.searchForStart(point.right, mins, maxs, (dimension+1)%2)
                
            
    def __init__(self, points):
        self.tree = self.createKDTree(points, 0)