from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    def search2(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return True
            elif nums[l] == nums[m]:
                l += 1
            elif nums[l] <= target < nums[m]:
                r = m - 1
            elif nums[m] < target <= nums[r]:
                l = m + 1
            elif nums[l] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        return False

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, get_sol().search( [1,0,1,1,1], 0 ))
    def test2(self):
        self.assertEqual(True, get_sol().search(  [3,4,1,3,3,3,3],4 ))
    def test3(self):
        self.assertEqual(True, get_sol().search( [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2 ))
    def test4(self):
        self.assertEqual(True, get_sol().search( [2,2,2,0,0,1], 0 ))
