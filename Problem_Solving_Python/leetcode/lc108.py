from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(lo,hi):
            if lo>hi:return None
            mid = (lo+hi)//2
            root = TreeNode(nums[mid])
            root.left=helper(lo,mid-1)
            root.right = helper(mid+1,hi)
            return root


        return helper(0,len(nums)-1)
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertIn(ser(get_sol().sortedArrayToBST([-10,-3,0,5,9])),['0,-3,9,-10,null,5','0,-10,5,null,-3,null,9'])
    def test02(self):
        self.assertIn(ser(get_sol().sortedArrayToBST([1,3])),['1,null,3','3,null,1'])
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
