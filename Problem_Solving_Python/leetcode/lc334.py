from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sub = []
        def binary_search(val):
            lo,hi=0,len(sub)-1
            while lo<=hi:
                mid = (lo+hi)//2
                if sub[mid]==val:
                    return mid
                elif sub[mid]<val:
                    lo=mid+1
                else:
                    hi=mid-1
            return lo
        for n in nums:
            if not sub:
                sub.append(n)
            elif n>sub[-1]:
                sub.append(n)
            else:
                idx = binary_search(n)
                sub[idx]=n
            if len(sub)==3:return True
        return False

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        self.assertEqual(True, solution.increasingTriplet([1,2,3,4,5]))

    def test_2(self):
        solution = Solution()
        self.assertEqual(False, solution.increasingTriplet([5,4,3,2,1]))

    def test_3(self):
        solution = Solution()
        self.assertEqual(True, solution.increasingTriplet([2,1,5,0,4,6]))

