import heapq
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxArea(self, h: int, w: int, hCuts: List[int], vCuts: List[int]) -> int:
        MOD = 10**9+7
        vCuts.sort()
        hCuts.sort()
        h_max=hCuts[0]
        v_max=vCuts[0]
        for i in range(len(hCuts)):
            if i==len(hCuts)-1:
                # x=h-hCuts[i]
                # print(x,end=" ")
                h_max=max(h_max, h- hCuts[i])
            else:
                # x=hCuts[i+1]-hCuts[i]
                # print(x,end=" ")
                h_max=max(h_max, hCuts[i + 1]- hCuts[i])
        # print()
        for i in range(len(vCuts)):
            if i==len(vCuts)-1:
                # x=w-vCuts[i]
                # print(x,end=" ")
                v_max=max(v_max, w- vCuts[i])
            else:
                # x=vCuts[i+1]-vCuts[i]
                # print(x,end=" ")
                v_max=max(v_max, vCuts[i + 1]- vCuts[i])
        # print()
        # print(h_max,v_max)
        return (h_max%MOD*v_max%MOD)

class tester(unittest.TestCase):
    def test_1(self):
        h = 5
        w = 4
        horizontalCuts = [1,2,4]
        verticalCuts = [1,3]
        Output= 4
        self.assertEqual(Output,get_sol().maxArea(h,w,horizontalCuts,verticalCuts))
    def test_2(self):
        h = 5
        w = 4
        horizontalCuts = [3,1]
        verticalCuts = [1]
        Output= 6
        self.assertEqual(Output,get_sol().maxArea(h,w,horizontalCuts,verticalCuts))
    def test_3(self):
        h = 5
        w = 4
        horizontalCuts = [3]
        verticalCuts = [3]
        Output= 9
        self.assertEqual(Output,get_sol().maxArea(h,w,horizontalCuts,verticalCuts))
    def test_4(self):
        h = 1000000000
        w = 1000000000
        horizontalCuts = [2]
        verticalCuts = [2]
        Output= 81
        self.assertEqual(Output,get_sol().maxArea(h,w,horizontalCuts,verticalCuts))
    # def test_5(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
