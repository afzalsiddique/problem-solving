import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # assign hat with person
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD=10**9+7
        def isOn(mask,i): return mask&(1<<i)
        def turnOn(mask,i): return mask|(1<<i)
        def countBits(mask):
            cnt=0
            while mask:
                mask=mask&(mask-1)
                cnt+=1
            return cnt
        @functools.lru_cache(None)
        def dfs(i, personMask): # ith hat
            if countBits(personMask)==noOfPersons:
                return 1
            if i==40:
                return 0

            res=dfs(i + 1, personMask)
            for person in persons[i]:
                if not isOn(personMask, person):
                    res+=dfs(i + 1, turnOn(personMask, person))
                    res%=MOD
            return res

        noOfPersons=len(hats)
        persons=[[] for _ in range(40)] # for every hat create its preferred person list
        for person,preferredHats in enumerate(hats):
            for hat in preferredHats:
                hat-=1
                persons[hat].append(person)
        return dfs(0,0)

class Solution2:
    # assign person with hat
    # tle
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD=10**9+7
        def isOn(mask,i): return mask&(1<<i)
        def turnOn(mask,i): return mask|(1<<i)
        @functools.lru_cache(None)
        def dfs(i,mask):
            if i==n:
                return 1
            res=0
            for hat in hats[i]:
                if not isOn(mask,hat):
                    res+=dfs(i+1,turnOn(mask,hat))
                    res%=MOD
            return res
        n=len(hats)
        return dfs(0,0)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(1,get_sol().numberWays([[3,4],[4,5],[5]]))
    def test2(self):
        self.assertEqual(4,get_sol().numberWays([[3,5,1],[3,5]]))
    def test3(self):
        self.assertEqual(24,get_sol().numberWays([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
    def test4(self):
        self.assertEqual(778256459,get_sol().numberWays([[1,2,4,6,7,8,9,11,12,13,14,15,16,18,19,20,23,24,25],[2,5,16],[1,4,5,6,7,8,9,12,15,16,17,19,21,22,24,25],[1,3,6,8,11,12,13,16,17,19,20,22,24,25],[11,12,14,16,18,24],[2,3,4,5,7,8,13,14,15,17,18,21,24],[1,2,6,7,10,11,13,14,16,18,19,21,23],[1,3,6,7,8,9,10,11,12,14,15,16,18,20,21,22,23,24,25],[2,3,4,6,7,10,12,14,15,16,17,21,22,23,24,25]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
