from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq=[]
        for x,y in points:
            heappush(pq,[-(abs(x*x)+abs(y*y)),x,y])
            if len(pq)>k:
                heappop(pq)
        return [[x,y] for _,x,y in pq]

class Solution2:
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

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([[-2,2]], get_sol().kClosest([[1,3],[-2,2]], 1))
    def test02(self):
        self.assertEqual(sorted([[3,3],[-2,4]]), sorted(get_sol().kClosest([[3,3],[5,-1],[-2,4]], 2)))
    def test03(self):
        self.assertEqual(sorted([[1,1],[3,3]]), sorted(get_sol().kClosest([[3,3],[5,-1],[-2,4],[1,1]], 2)))
    # def test04(self):
    # def test05(self):
    # def test06(self):
