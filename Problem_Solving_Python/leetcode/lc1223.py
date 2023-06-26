from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # assume that die has numbers from [0,5]
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        M=10**9+7
        @cache
        def dp(i, prevNum):
            if i==n:
                return 1
            if i>n:
                return 0
            res=0
            for num in range(6):
                if num==prevNum:
                    continue
                for cnt in range(1,rollMax[num]+1):
                    res+=dp(i+cnt,num)
                    res%=M
            return res

        return dp(0,-1)
class Solution2:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD=10**9+7
        # def dp(n:int,lastNum:int,lastNumFreq:int,path:List[int]):
        @cache
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
    def test5(self):
        self.assertEqual(31, get_sol().dieSimulator(n = 2, rollMax = [2,1,1,1,1,1]))
    # def test6(self):
    # def test7(self):

