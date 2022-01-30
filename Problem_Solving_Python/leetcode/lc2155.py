from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def myord(char):
            return ord(char)-ord('a')+1

        s=s[::-1]
        n=k
        m = len(s)
        j = 0
        t = 0    # hash value for txt
        h = 1

        for i in range(n-1):
            h = (h * power) % modulo

        for i in range(n):
            t = (t*power + myord(s[i]))    % modulo

        for i in range(m-n + 1):
            if hashValue == t:
                res=s[i:i+n]

            if i < m-n:
                t = t-myord(s[i])*h
                t = t * power
                t = t+myord(s[i+n])
                t = t % modulo
                if t < 0:
                    t = t + modulo
        return res[::-1]

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual('ee', get_sol().subStrHash("leetcode",  7,  20, 2,  0))
    def test02(self):
        self.assertEqual('ih', get_sol().subStrHash("ihg",  10,  100000, 2,  89))
    def test03(self):
        self.assertEqual('hg', get_sol().subStrHash("ihg",  10,  100000, 2,  78))
    def test04(self):
        self.assertEqual('fbx', get_sol().subStrHash(s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32))
    # def test05(self):
