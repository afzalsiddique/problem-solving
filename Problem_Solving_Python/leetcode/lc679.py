import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/24-game/discuss/113972/Very-Easy-JAVA-DFS
    EPSILON = 0.001
    def judgePoint24(self, nums: List[int]) -> bool:
        lst = [float(num) for num in nums] # convert each integer to a float and add to the list
        return self.dfs(lst)

    def dfs(self, lst):
        if len(lst) == 1:
            return abs(lst[0] - 24) < self.EPSILON # if close enough to 24
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                next_lst = [lst[k] for k in range(len(lst)) if k not in [i,j]] # create new list for next recursive call
                for result in self.generatePossibleResults(lst[i], lst[j]):
                    next_lst.append(result) # add all non-used numbers to the new list
                    if self.dfs(next_lst):
                        return True
                    next_lst.pop() # backtracking
        return False

    def generatePossibleResults(self, x, y):
        results = []
        results.append(x + y)
        results.append(x - y)
        results.append(y - x)
        results.append(x * y)
        if y != 0:
            results.append(x / y)
        if x != 0:
            results.append(y / x)
        return results
class Solution2:
    epsilon=0.001
    def judgePoint24(self, nums):
        if len(nums)==1: return abs(nums[0]-24)<self.epsilon
        for i in range(len(nums)): # i=right_index
            for j in range(i): # j=left_index
                a=nums.pop(i)
                b=nums.pop(j)
                nxt=[a+b,a-b,b-a,a*b]
                if abs(a)>self.epsilon: # if a is not zero
                    nxt.append(b/a)
                if abs(b)>self.epsilon: # if b is not zero
                    nxt.append(a/b)
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
