from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int):
        return self.mergeSort(points)[:K]

    def mergeSort(self, points):
        if len(points) > 1:
            mid = len(points) // 2
            L = points[:mid]
            R = points[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][0] ** 2 + L[i][1] ** 2 < R[j][0] ** 2 + R[j][1] ** 2:
                    points[k] = L[i]
                    i += 1
                else:
                    points[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                points[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                points[k] = R[j]
                j += 1
                k += 1
        return points
