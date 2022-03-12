from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    # https://www.youtube.com/watch?v=edJ19qIL8WQ
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=bisect_left(nums,target)
        if left==n or nums[left]!=target:
            return [-1,-1]
        right=bisect_right(nums,target)
        if right==0 or nums[right-1]!=target:
            return [left,-1]
        return [left,right-1]


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([3,4], get_sol().searchRange( [5,7,7,8,8,10],  8))
    def test02(self):
        self.assertEqual([-1,-1], get_sol().searchRange( [5,7,7,8,8,10],  6))
    def test03(self):
        self.assertEqual([-1,-1], get_sol().searchRange( [],  0))
    def test04(self):
        self.assertEqual([4,4], get_sol().searchRange( [5,7,7,7,8,10],  8))

