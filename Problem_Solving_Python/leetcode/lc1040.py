import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numMovesStonesII(self, stones):
        stones.sort()
        i,j=0,0
        n=len(stones)
        low=len(stones)
        gaps=[stones[i]-stones[i-1]-1 for i in range(1,len(stones))] # empty spaces between two stones
        high = sum(gaps)-min(gaps[0],gaps[-1]) # https://leetcode.com/problems/moving-stones-until-consecutive-ii/discuss/289357/c%2B%2B-with-picture
        while j<n:
            while stones[j] - stones[i] >= n:
                i += 1

            # if A[i:j] contains all stones except one stone and the stones are positioned consecutively
            if            j - i + 1 == n - 1                 and stones[j] - stones[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
            j+=1
        return [low, high]

class MyTestCase(unittest.TestCase):
    def test_1(self):
        stones = [7,4,9]
        Output= [1,2]
        self.assertEqual(Output, get_sol().numMovesStonesII(stones))
    def test_2(self):
        stones = [3,4,5,6,100]
        Output= [2,93]
        self.assertEqual(Output, get_sol().numMovesStonesII(stones))
    def test_3(self):
        stones = [3,4,5,7,100]
        Output= [1,93]
        self.assertEqual(Output, get_sol().numMovesStonesII(stones))
    def test_4(self):
        stones = [6,5,4,3,10]
        Output= [2,3]
        self.assertEqual(Output, get_sol().numMovesStonesII(stones))
    def test_5(self):
        stones = [2,9,18,20,29,33,36,38,46]
        Output= [6,30]
        self.assertEqual(Output, get_sol().numMovesStonesII(stones))
    def test_6(self):
        stones = [1,500000000,1000000000]
        Output= [2,499999999]
        self.assertEqual(Output, get_sol().numMovesStonesII(stones))
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
