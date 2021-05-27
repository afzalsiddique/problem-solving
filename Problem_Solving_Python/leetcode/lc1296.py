import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution2()
class Solution:
    # wrong
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        def create_forward(x):
            for i in range(k):
                if not remaining[x+i]: return False
            for i in range(k):
                remaining[x+i]-=1
            return True
        def create_backward(x):
            for i in range(k):
                if not remaining[x-i]: return False
            for i in range(k):
                remaining[x-i]-=1
            return True

        remaining = defaultdict(int)
        for x in nums: remaining[x]+=1

        for x in nums:
            if not remaining[x]: continue
            forward = create_forward(x)
            backward = create_backward(x)
            if not forward and not backward: return False
        return True
class Solution2:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        remaining = Counter(nums)

        nums.sort()
        for x in nums:
            if not remaining[x]: continue
            for i in range(k):
                if not remaining[x+i]: return False
                remaining[x+i]-=1
        return True
class tester(unittest.TestCase):
    def test1(self):
        nums = [1,2,3,3,4,4,5,6]
        k = 4
        Output= True
        self.assertEqual(Output,get_sol().isPossibleDivide(nums,k))
    def test2(self):
        nums = [3,2,1,2,3,4,3,4,5,9,10,11]
        k = 3
        Output= True
        self.assertEqual(Output,get_sol().isPossibleDivide(nums,k))
    def test3(self):
        nums = [3,3,2,2,1,1]
        k = 3
        Output= True
        self.assertEqual(Output,get_sol().isPossibleDivide(nums,k))
    def test4(self):
        nums = [1,2,3,4]
        k = 3
        Output= False
        self.assertEqual(Output,get_sol().isPossibleDivide(nums,k))
    def test5(self):
        nums = [10,9,8,1,2,3,2,3,4,4,5,6,10,11,12]
        k = 3
        Output= True
        self.assertEqual(Output,get_sol().isPossibleDivide(nums,k))
    def test6(self):
        nums = [12,12,2,11,22,20,11,13,3,21,1,13]
        k = 3
        Output= True
        self.assertEqual(Output,get_sol().isPossibleDivide(nums,k))