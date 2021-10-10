import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution2()
# class Solution:
    # possible in O(n) time
    # def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

class Solution2:
    # sort increasingly on attack and decreasingly on defense.
    # sorting decreasingly on defense can get rid of items which have same attack values
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        stack = [] # decreasing stack
        ans = 0
        for _, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                ans += 1
            stack.append(d)
        return ans
        # return len(properties)-len(stack) # also works

class Solution3:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        stack = [] # increasing stack
        ans = 0
        for i in reversed(range(len(properties))):
            _,d = properties[i]
            while stack and stack[-1] > d:
                stack.pop()
                ans += 1
            stack.append(d)
        return ans
        # return len(properties)-len(stack) # also works


class MyTestCase(unittest.TestCase):
    def test1(self):
        properties = [[5,5],[6,3],[3,6]]
        Output= 0
        self.assertEqual(Output, get_sol().numberOfWeakCharacters(properties))
    def test2(self):
        properties = [[2,2],[3,3]]
        Output= 1
        self.assertEqual(Output, get_sol().numberOfWeakCharacters(properties))
    def test3(self):
        properties = [[1,5],[10,4],[4,3]]
        Output= 1
        self.assertEqual(Output, get_sol().numberOfWeakCharacters(properties))
    def test4(self):
        properties = [[1,1],[2,1],[2,2],[1,2]]
        Output= 1
        self.assertEqual(Output, get_sol().numberOfWeakCharacters(properties))
    def test5(self):
        properties = [[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]]
        Output= 6
        self.assertEqual(Output, get_sol().numberOfWeakCharacters(properties))
    # def test6(self):
