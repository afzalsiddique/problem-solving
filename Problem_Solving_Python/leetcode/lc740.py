import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(n)
    # space O(n) for creating gold array otherwise space O(1)
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        BIG = 20001
        gold = [0]*BIG
        for num in nums:
            gold[num]+=num
        second_last=gold[0]
        last=max(gold[0],gold[1])
        for i in range(2,BIG):
            cur = max(gold[i]+second_last, last)
            second_last=last
            last=cur
        return max(last,second_last)


class tester(unittest.TestCase):
    def test01(self):
        nums = [3,4,2]
        Output= 6
        self.assertEqual(Output,get_sol().deleteAndEarn(nums))
    def test02(self):
        nums = [2,2,3,3,3,4]
        Output= 9
        self.assertEqual(Output,get_sol().deleteAndEarn(nums))