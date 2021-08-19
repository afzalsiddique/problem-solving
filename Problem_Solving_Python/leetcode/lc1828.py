from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # binary search
    # Time O(PlogP + QlogP). Space O(Q)
    # https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/discuss/1163070/Short-and-Easy-Solution-w-Explanation-or-Distance-bw-point-and-Circle-Center/911447
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def within_circle(x1,y1,x2,y2,r):
            return (x1-x2)**2 + (y1-y2)**2 <= r**2
        points.sort(key=lambda x: x[0])
        n = len(queries)
        res =[0]*n
        for i in range(n):
            x1, y1, r = queries[i]
            left = self.my_bisect_left(points, x1 - r)
            right = self.my_bisect_right(points, x1 + r)
            for j in range(left, right):
                x2, y2 = points[j]
                if within_circle(x1,y1,x2,y2,r):
                    res[i] += 1
        return res

    def my_bisect_left(self, arr, x):
        lo=0
        hi=len(arr)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if x<=arr[mid][0]: # compare with x coordinate
                hi=mid-1
            else:
                lo=mid+1
        return lo

    def my_bisect_right(self, arr, x):
        lo=0
        hi=len(arr)-1
        while lo<=hi:
            mid = lo+(hi-lo)//2
            if x>=arr[mid][0]: # compare with x coordinate
                lo=mid+1
            else:
                hi=mid-1
        return lo
class Solution2:
    # brute force
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def distance(x1,y1,x2,y2):
            x=abs(x1-x2)
            y=abs(y1-y2)
            return math.sqrt(x*x+y*y)
        n=len(queries)
        ans=[0]*n
        for i in range(len(queries)):
            x1,y1,r=queries[i]
            for x2,y2 in points:
                if distance(x1,y1,x2,y2)<=r:
                    ans[i]+=1
        return ans

class MyTestCase(unittest.TestCase):
    def test_1(self):
        points,queries = [[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]
        Output= [3,2,2]
        self.assertEqual(Output, get_sol().countPoints(points,queries))
    def test_2(self):
        points,queries = [[1,1],[2,2],[3,3],[4,4],[5,5]],[[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
        Output= [2,3,2,4]
        self.assertEqual(Output, get_sol().countPoints(points,queries))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):