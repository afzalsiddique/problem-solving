import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=eEvLI9i02Zw
    def splitArray(self, nums: List[int], m: int) -> int:
        def feasible(mid, m):
            cnt=1
            total=0
            for n in nums:
                total+=n
                if total>mid:
                    cnt+=1
                    total=n
            if cnt>m: return False
            return True

        left=max(nums)
        right=sum(nums)
        while left<=right:
            mid = (left+right)//2
            if feasible(mid,m):
                right=mid-1
            else:
                left=mid+1
        return left

class tester(unittest.TestCase):
    def test01(self):
        nums = [7,2,5,10,8]
        m = 2
        Output= 18
        self.assertEqual(Output,get_sol().splitArray(nums,m))
    def test02(self):
        nums = [1,2,3,4,5]
        m = 2
        Output= 9
        self.assertEqual(Output,get_sol().splitArray(nums,m))
    def test03(self):
        nums = [1,4,4]
        m = 3
        Output= 4
        self.assertEqual(Output,get_sol().splitArray(nums,m))
