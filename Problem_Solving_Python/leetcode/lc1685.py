import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre_sum=list(itertools.accumulate(nums))
        res=[]
        for i in range(n):
            if i==0:
                left=0
            else:
                left=pre_sum[i-1]
            if i==n-1:
                right=0
            else:
                right=pre_sum[-1]-pre_sum[i]
            ans=nums[i]*i-left  +  right-nums[i]*(n-1-i)
            res.append(ans)
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [2,3,5]
        Output= [4,3,5]
        self.assertEqual(Output, get_sol().getSumAbsoluteDifferences(nums))
    def test_2(self):
        nums = [1,4,6,8,10]
        Output= [24,15,13,15,21]
        self.assertEqual(Output, get_sol().getSumAbsoluteDifferences(nums))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):