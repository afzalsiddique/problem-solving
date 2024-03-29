from heapq import *; import unittest; from typing import List;


def get_sol(): return Solution()
class MaxHeap(list):
    # https://leetcode.com/problems/max-value-of-equation/discuss/709231/JavaPython-Priority-Queue-and-Deque-Solution-O(N)
    # Because xi < xj,
    # yi + yj + |xi - xj| = (yi - xi) + (yj + xj)
    # we will get (yi-xi) from the heap
    # So for each pair of (xj, yj),
    # we have xj + yj, and we only need to find out the maximum yi - xi
    def __init__(self): super().__init__()
    def top(self): return -self[0]
    def topYminusX(self): return -self[0][0]
    def topX(self): return -self[0][1]
    def push(self, price, amount): heappush(self, [-price, -amount])
    def heappop(self): return heappop(self)
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        maxHeap=MaxHeap()
        res=float('-inf')
        for x,y in points:
            while maxHeap and x-maxHeap.topX()>k: # x is greater than topX as per given condition
                maxHeap.heappop()
            if maxHeap:
                res=max(res, maxHeap.topYminusX() + x + y)
            maxHeap.push(y-x,x)
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4,get_sol().findMaxValueOfEquation(points = [[1,3],[2,0],[5,10],[6,-10]], k = 1))
    def test02(self):
        self.assertEqual(3,get_sol().findMaxValueOfEquation(points = [[0,0],[3,0],[9,2]], k = 3))
    def test03(self):
        self.assertEqual(35,get_sol().findMaxValueOfEquation([[-19,-12],[-13,-18],[-12,18],[-11,-8],[-8,2],[-7,12],[-5,16],[-3,9],[1,-7],[5,-4],[6,-20],[10,4],[16,4],[19,-9],[20,19]], 6))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
