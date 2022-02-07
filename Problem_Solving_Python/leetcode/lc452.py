# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/93735/A-Concise-Template-for-%22Overlapping-Interval-Problem%22
from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
## similar ###
# 56 Merge Intervals
# 435 Non-overlapping Intervals
# 252 Meeting Rooms
# 253 Meeting Rooms II

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # if len(points)==0:return 0
        points.sort(key=lambda x:x[1])
        shoot, res = float('-inf'),0
        shoots = []
        for start,end in points:
            if shoot<start:
                res+=1
                shoot=end
                shoots.append(shoot)
        print(shoots)
        return res

    def findMinArrowShots2(self, points):
        points.sort(reverse=True)
        shoot,res = float('inf'), 0
        shoots = []
        for start, end in points:
            if shoot > end:
                res += 1
                shoot = start
                shoots.append(shoot)
        print(shoots)
        return res

    def findMinArrowShots3(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        res ,shoot= 0,-1
        for start, end in points:
            if start<=shoot<=end: continue
            shoot = end
            res+=1
        return res



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
    def test02(self):
        self.assertEqual(4, get_sol().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
    def test03(self):
        self.assertEqual(2, get_sol().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
    def test04(self):
        self.assertEqual(1, get_sol().findMinArrowShots([[1,2]]))
    def test05(self):
        self.assertEqual(1, get_sol().findMinArrowShots([[2,3],[2,3]]))
    def test06(self):
        self.assertEqual(0, get_sol().findMinArrowShots([]))
    def test07(self):
        self.assertEqual(1, get_sol().findMinArrowShots([[-2147483648,2147483647]]))