from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution4()

# Find Minimum in Rotated Sorted Array I----no duplicate ----O(logN)
# https://www.youtube.com/watch?v=OXkLNPalfRs
class Solution:
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi -lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

# Find Minimum in Rotated Sorted Array II----contain duplicates----O(logN)~O(N)
# https://www.youtube.com/watch?v=K0PjrikGKK4
class Solution2:
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid if nums[hi] != nums[mid] else hi - 1
        return nums[lo]

class Solution3:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        lo,hi=0,n
        while lo<hi:
            mid=(lo+hi)//2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] >= nums[lo] and nums[mid] > nums[hi-1]:
                lo = mid+1
            elif nums[mid] <= nums[hi-1] and nums[mid] <= nums[lo]:
                hi = mid
            elif nums[mid] <= nums[hi-1] and nums[mid] >= nums[lo]:
                hi = mid
        return nums[lo]

class Solution4:
    def findMin(self, nums: List[int]) -> int:
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if hi-lo+1<=2: return min(nums[lo],nums[hi])

            # not necessary
            # if hi-lo+1==3: return min(nums[lo],nums[mid],nums[hi])

            if nums[lo]<nums[mid] and nums[mid]<nums[hi]:
                return nums[lo]
            elif nums[mid]<nums[hi]:
                hi=mid
            else:
                lo=mid+1


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().findMin([3,4,5,1,2]))
    def test1(self):
        self.assertEqual(1,get_sol().findMin([1]))
    def test2_1(self):
        self.assertEqual(1,get_sol().findMin([1,2]))
    def test2_2(self):
        self.assertEqual(1,get_sol().findMin([2,1]))
    def test3_1(self):
        self.assertEqual(1,get_sol().findMin([1,2,3]))
    def test3_2(self):
        self.assertEqual(1,get_sol().findMin([3,1,2]))
    def test3_3(self):
        self.assertEqual(1,get_sol().findMin([2,3,1]))
    def test4_1(self):
        self.assertEqual(1,get_sol().findMin([1,2,3,4]))
    def test4_2(self):
        self.assertEqual(1,get_sol().findMin([4,1,2,3]))
    def test4_3(self):
        self.assertEqual(1,get_sol().findMin([3,4,1,2]))
    def test4_4(self):
        self.assertEqual(1,get_sol().findMin([2,3,4,1]))
    def test5_1(self):
        self.assertEqual(1,get_sol().findMin([1,2,3,4,5]))
    def test5_2(self):
        self.assertEqual(1,get_sol().findMin([5,1,2,3,4]))
    def test5_3(self):
        self.assertEqual(1,get_sol().findMin([4,5,1,2,3]))
    def test5_4(self):
        self.assertEqual(1,get_sol().findMin([3,4,5,1,2]))
    def test5_5(self):
        self.assertEqual(1,get_sol().findMin([2,3,4,5,1]))
    def test2(self):
        self.assertEqual(0,get_sol().findMin([4,5,6,7,0,1,2]))
    def test3(self):
        self.assertEqual(11,get_sol().findMin([11,13,15,17]))
