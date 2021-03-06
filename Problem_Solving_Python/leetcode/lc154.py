import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



# Find Minimum in Rotated Sorted Array I----no duplicate ----O(logN)
# https://www.youtube.com/watch?v=OXkLNPalfRs
class Solution:
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
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



class tester(unittest.TestCase):
    def test1(self):
        nums = [1,3,5]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test2(self):
        nums = [2,2,2,0,1]
        Output= 0
        self.assertEqual(Output,Solution().findMin(nums))
    def test4(self):
        nums = [2,2,2,2,1,1,2]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test1_1(self):
        nums = [1]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))

    def test2_1(self):
        nums = [1,2]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test2_2(self):
        nums = [2,1]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))

    def test3_1(self):
        nums = [1,2,3]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test3_2(self):
        nums = [3,1,2]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test3_3(self):
        nums = [2,3,1]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))

    def test4_1(self):
        nums = [1,2,3,4]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test4_2(self):
        nums = [4,1,2,3]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test4_3(self):
        nums = [3,4,1,2]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test4_4(self):
        nums = [2,3,4,1]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))

    def test5_1(self):
        nums = [1,2,3,4,5]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test5_2(self):
        nums = [5,1,2,3,4]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test5_3(self):
        nums = [4,5,1,2,3]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test5_4(self):
        nums = [3,4,5,1,2]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))
    def test5_5(self):
        nums = [2,3,4,5,1]
        Output= 1
        self.assertEqual(Output,Solution().findMin(nums))

    def test2(self):
        nums = [4,5,6,7,0,1,2]
        Output= 0
        self.assertEqual(Output,Solution().findMin(nums))
    def test3(self):
        nums = [11,13,15,17]
        Output= 11
        self.assertEqual(Output,Solution().findMin(nums))
