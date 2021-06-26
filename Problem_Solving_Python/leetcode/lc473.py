import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n=len(matchsticks)
        def put(i):
            if i==n: return True
            for buck_idx in range(len(buckets)):
                if matchsticks[i]+buckets[buck_idx]>target: continue
                buckets[buck_idx]+=matchsticks[i]
                if put(i + 1): return True
                buckets[buck_idx]-=matchsticks[i]
                if buckets[buck_idx]==0:
                    return False # optimization
            return False

        k=4
        buckets=[0]*k
        matchsticks.sort(reverse=True) # optimization
        target=sum(matchsticks)//k
        return put(0)

class Solution2:
    # tle
    # time O(k*2^n)
    def makesquare(self, matchsticks: List[int]) -> bool:
        n=len(matchsticks)
        vis=set()
        def divide_k_equal_subset(k, cur_sum):
            if k==1: return True
            if cur_sum==target:
                return divide_k_equal_subset(k - 1, 0)
            if cur_sum>target:
                return False
            for i in range(n):
                if i in vis: continue
                vis.add(i)
                if divide_k_equal_subset(k,cur_sum+matchsticks[i]): return True
                vis.remove(i)
            return False

        k=4
        summ = sum(matchsticks)
        target=summ//k
        if summ%k!=0: return False
        for num in matchsticks:
            if num>target: return False
        return divide_k_equal_subset(k,0)


class tester(unittest.TestCase):
    def test01(self):
        matchsticks = [1,1,2,2,2]
        Output= True
        self.assertEqual(Output,get_sol().makesquare(matchsticks))
    def test02(self):
        matchsticks = [3,3,3,3,4]
        Output= False
        self.assertEqual(Output,get_sol().makesquare(matchsticks))
    def test03(self):
        matchsticks = [2,2,2,2,2,6]
        Output= False
        self.assertEqual(Output,get_sol().makesquare(matchsticks))
    def test04(self):
        matchsticks = [6,6,6,6,4,2,2]
        Output= False
        self.assertEqual(Output,get_sol().makesquare(matchsticks))
    def test05(self):
        matchsticks = [211559,9514615,7412176,5656677,3816020,452925,7979371,5025276,8882605,944541,9889007,2344356,7252152,749758,2311818]
        Output= False
        self.assertEqual(Output,get_sol().makesquare(matchsticks))
