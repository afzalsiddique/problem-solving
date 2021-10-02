import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # sliding window
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        preSum = list(itertools.accumulate(nums))

        def getSum(left, right):  # left, right inclusive
            return preSum[right] - preSum[left] + nums[left]
        def valid(l,r): # we are trying to increment in range [l,r-1] (inclusive) and make them equal to nums[r]
            s = getSum(l,r-1)
            return s+k>=( (r-1) -l + 1) * nums[r]

        l=0
        r = 0
        ans = 1
        while r<n:
            if l==r:
                r+=1
            elif valid(l,r): # found an answer. try to find a better answer
                ans = max(ans,r-l+1)
                r+=1
            else:
                l+=1
        return ans
class Solution2:
    # binary search
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        preSum = list(itertools.accumulate(nums))

        def getSum(left, right):  # left, right inclusive
            return preSum[right] - preSum[left] + nums[left]

        def valid(index,mid):
            s = getSum(mid, index - 1)
            return s + k >= (index - mid) * nums[index]

        def count(index): # Count frequency of `nums[index]` if we make other elements equal to `nums[index]`
            left = 0
            right = index - 1
            res = index
            while left <= right:
                mid = left + (right - left) // 2
                if valid(index,mid): # Found an answer -> Try to find a better answer in the left side
                    res = mid  # save best answer so far
                    right = mid - 1
                else:
                    left = mid + 1

            return index - res + 1 # +1 is the default value

        ans = 0
        for i in range(n):
            ans = max(ans, count(i))
        return ans

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums,k = [1,2,4], 5
        Output= 3
        self.assertEqual(Output, get_sol().maxFrequency(nums,k))
    def test_2(self):
        nums,k = [1,4,8,13], 5
        Output= 2
        self.assertEqual(Output, get_sol().maxFrequency(nums,k))
    def test_3(self):
        nums,k = [3,9,6], 2
        Output= 1
        self.assertEqual(Output, get_sol().maxFrequency(nums,k))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
