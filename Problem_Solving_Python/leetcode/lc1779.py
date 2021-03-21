from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def valid(point):
            if point[0] == x:return True
            if point[1] == y: return True
            return False
        def manhattan(point):
            return abs(point[0]-x) + abs(point[1]-y)

        idx,minn = -1, float('inf')
        for i in range(len(points)):
            if valid(points[i]):
                dist = manhattan(points[i])
                if dist<minn:
                    minn = dist
                    idx = i

        return idx
