from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        maxx = -1
        while left != right:
            if height[left] < height[right]:
                limited_by_left = True
            else:
                limited_by_left = False
            area = min(height[left], height[right]) * (right - left)
            if area > maxx:
                maxx = area

            if limited_by_left:
                left += 1
            else:
                right -= 1
        return maxx

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(49, get_sol().maxArea(height = [1,8,6,2,5,4,8,3,7]))
    def test02(self):
        self.assertEqual(1, get_sol().maxArea(height = [1,1]))
    def test03(self):
        self.assertEqual(16, get_sol().maxArea(height = [4,3,2,1,4]))
    def test04(self):
        self.assertEqual(2, get_sol().maxArea(height = [1,2,1]))
    def test05(self):
        self.assertEqual(8, get_sol().maxArea([1,0,0,0,0,0,0,2,2]))
