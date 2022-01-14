import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def makesquare(self, A):
        def put(index): # dfs
            if index==len(A): return True
            seen=set()
            for i in range(k):
                if buckets[i]+A[index]>target: continue
                if buckets[i] in seen: continue # optimization
                seen.add(buckets[i])
                buckets[i]+=A[index]
                if put(index+1):
                    return True
                buckets[i]-=A[index]
                # if buckets[i]==0: return False # optimization
            return False

        A.sort(reverse=True) # optimization
        k=4
        summ=sum(A)
        target=summ//k
        if len(A) < k or sum(A) % k != 0 or max(A) > target:
            return False
        buckets=[0]*k
        return put(0)
class Solution2:
    def makesquare(self, A):
        def put(index): # dfs
            if index==len(A): return True
            for i in range(k):
                if buckets[i]+A[index]>target: continue
                if i>0 and buckets[i]==buckets[i-1]: # we have already tried to put the matchstick in (i-1)th bucket with the same value
                    continue # optimization
                buckets[i]+=A[index]
                if put(index+1):
                    return True
                buckets[i]-=A[index]
                # if buckets[i]==0: return False # optimization
            return False

        A.sort(reverse=True) # optimization
        k=4
        summ=sum(A)
        target=summ//k
        if len(A) < k or sum(A) % k != 0 or max(A) > target:
            return False
        buckets=[0]*4
        return put(0)
class Solution4:
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



class Tester(unittest.TestCase):
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
    def test06(self):
        matchsticks = [1,1,1,1,1,1,1,1,1,1,1,1,4,4,4]
        Output= True
        self.assertEqual(Output,get_sol().makesquare(matchsticks))
    def test07(self):
        matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
        Output= True
        self.assertEqual(Output,get_sol().makesquare(matchsticks))
