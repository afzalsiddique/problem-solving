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

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
print(nearestValidPoint(x,y,points))


x = 3
y = 4
points = [[3,4]]
print(nearestValidPoint(x,y,points))


x = 3
y = 4
points = [[2,3]]
print(nearestValidPoint(x,y,points))
