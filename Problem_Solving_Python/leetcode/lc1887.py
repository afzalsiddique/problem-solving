import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        smallest = nums[0]
        dp = {}
        def f(num):
            if num==smallest:
                return 0
            if num in dp: return dp[num]
            idx = bisect_left(nums, num)
            dp[num] = 1 + f(nums[idx-1])
            return dp[num]

        res=0
        for num in nums:
            res+= f(num)
        return res

class Solution2:
    # tle
    def reductionOperations(self, nums: List[int]) -> int:
        di = Counter(nums)
        pq=[]
        for x in di:
            pq.append((-x,di[x]))
        heapify(pq)
        cnt = 0
        while len(pq)!=1:
            cnt+=1
            x1,freq1 = heappop(pq)
            x2,freq2 = heappop(pq)
            x1*=-1
            x2*=-1
            heappush(pq,(-x2,freq2+1))
            if freq1!=1:
                heappush(pq,(-x1,freq1-1))
        return cnt



class tester(unittest.TestCase):
    def test1(self):
        nums = [5,1,3]
        Output= 3
        self.assertEqual(Output,get_sol().reductionOperations(nums))
    def test2(self):
        nums = [1,1,1]
        Output= 0
        self.assertEqual(Output,get_sol().reductionOperations(nums))
    def test3(self):
        nums = [1,1,2,2,3]
        Output= 4
        self.assertEqual(Output,get_sol().reductionOperations(nums))
