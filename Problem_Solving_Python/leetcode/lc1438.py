import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()


class Solution:
    # https://www.youtube.com/watch?v=LDFZm4iB7tA
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n=len(nums)
        min_q=deque()
        max_q=deque()
        ans=0
        left,right=0,0
        while right<n:
            x = nums[right]
            while min_q and nums[min_q[-1]]>=x: min_q.pop()
            while max_q and nums[max_q[-1]]<=x: max_q.pop()
            min_q.append(right)
            max_q.append(right)
            mini=nums[min_q[0]]
            maxi=nums[max_q[0]]
            if maxi-mini>limit:
                left+=1
                if left>min_q[0]: min_q.popleft()
                if left>max_q[0]: max_q.popleft()
            else:
                ans=max(ans,right-left+1)
                right+=1
        return ans


class tester(unittest.TestCase):
    def test1(self):
        nums = [8,2,4,7]
        limit = 4
        Output= 2
        self.assertEqual(Output,get_sol().longestSubarray(nums,limit))
    def test2(self):
        nums = [10,1,2,4,7,2]
        limit = 5
        Output= 4
        self.assertEqual(Output,get_sol().longestSubarray(nums,limit))
    def test3(self):
        nums = [4,2,2,2,4,4,2,2]
        limit = 0
        Output= 3
        self.assertEqual(Output,get_sol().longestSubarray(nums,limit))
