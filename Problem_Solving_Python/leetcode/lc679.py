import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/24-game/discuss/113972/Very-Easy-JAVA-DFS
    def judgePoint24(self, nums):
        return
class Solution2:
    epsilon=0.001
    def judgePoint24(self, nums):
        if len(nums)==1: return abs(nums[0]-24)<self.epsilon
        for i in range(len(nums)): # i=right_index
            for j in range(i): # j=left_index
                a=nums.pop(i)
                b=nums.pop(j)
                nxt=[a+b,a-b,b-a,a*b]
                if abs(a)>self.epsilon: nxt.append(b/a)
                if abs(b)>self.epsilon: nxt.append(a/b)
                for n in nxt:
                    nums.append(n)
                    if self.judgePoint24(nums): return True
                    nums.pop()
                nums.add(j, b)  # j should be put back first
                nums.add(i, a)
        return False



class MyTestCase(unittest.TestCase):
    def test1(self):
        cards = [4,1,8,7]
        Output= True
        self.assertEqual(Output, get_sol().judgePoint24(cards))
    def test2(self):
        cards = [1,2,1,2]
        Output= False
        self.assertEqual(Output, get_sol().judgePoint24(cards))
    def test3(self):
        cards = [1,5,9,1]
        Output= False
        self.assertEqual(Output, get_sol().judgePoint24(cards))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
