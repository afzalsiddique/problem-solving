import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        seen=set()
        res=float('inf')
        for x1,y1 in points:
            for (x2,y2) in seen:
                # x1,y1 and x2,y2 are opposite points pair
                # now check if another opposite points pair exists
                if (x1,y2) in seen and (x2,y1) in seen:
                    area=abs(x1-x2)*abs(y1-y2)
                    if area>0 and area<res:
                        res=area
            seen.add((x1,y1))
        return res if res!=float('inf') else 0

class tester(unittest.TestCase):
    def test01(self):
        points= [[1,1],[1,3],[3,1],[3,3],[2,2]]
        Output= 4
        self.assertEqual(Output, get_sol().minAreaRect(points))
    def test02(self):
        points= [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
        Output= 2
        self.assertEqual(Output, get_sol().minAreaRect(points))
    def test03(self):
        points= [[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]]
        Output= 0
        self.assertEqual(Output, get_sol().minAreaRect(points))
