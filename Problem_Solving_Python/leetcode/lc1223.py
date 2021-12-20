import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD=10**9+7
        # def dp(n:int,lastNum:int,lastNumFreq:int,path:List[int]):
        @functools.lru_cache(None)
        def dp(n:int,lastNum:int,lastNumFreq:int):
            if n==0:
                # li.append(path[:])
                return 1
            res=0
            for i in range(6):
                limit=rollMax[i]
                if lastNum==i:
                    if lastNumFreq+1>limit: continue
                    # res+=dp(n-1,i,lastNumFreq+1,path+[i])
                    res+=dp(n-1,i,lastNumFreq+1)
                else:
                    # res+=dp(n-1,i,1,path+[i])
                    res+=dp(n-1,i,1)
                res%=MOD
            return res

        # li=[]
        # res= dp(n,-1,0,[])
        res= dp(n,-1,0)
        # for x in li: print(x)
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(34, get_sol().dieSimulator(n = 2, rollMax = [1,1,2,2,2,3]))
    def test2(self):
        self.assertEqual(30, get_sol().dieSimulator(n = 2, rollMax = [1,1,1,1,1,1]))
    def test3(self):
        self.assertEqual(181, get_sol().dieSimulator(n = 3, rollMax = [1,1,1,2,2,3]))
    def test4(self):
        self.assertEqual(822005673, get_sol().dieSimulator(20, [8,5,10,8,7,2]))
    # def test5(self):
    # def test6(self):
    # def test7(self):

