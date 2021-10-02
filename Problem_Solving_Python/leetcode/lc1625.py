import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(10*10*n)
    # 1. Without rotation, in worst case we have 10 strings due to "add a" operation;
    # 2. With rotations, for each string in step 1, in worst case we can have n new strings, where n = s.length();
    # 3. For each string in step 2, if b is odd, in worst case we can create 10 strings due to "add a" operation; (
    #       Note: if b is even, then no new strings can be created during this step.)

    # dfs
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = [int(x) for x in s]
        minn=s[:]
        visited = set()
        def apply_op1(s:list):
            option1 = []
            for i,x in enumerate(s):
                if i&1:
                    option1.append((x+a)%10)
                else:
                    option1.append(x)
            return option1
        def dfs(s:list):
            nonlocal minn
            tmp=''.join(str(x) for x in s)
            if tmp in visited: return
            visited.add(tmp)
            option1 = apply_op1(s)
            option2 = s[-b:]+s[:-b]
            minn=min(minn,s,option1,option2)
            dfs(option1)
            dfs(option2)
            return

        dfs(s)
        return ''.join(str(x) for x in minn)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s,a,b = "5525",  9,  2
        Output= "2050"
        self.assertEqual(Output, get_sol().findLexSmallestString(s,a,b))
    def test_2(self):
        s,a,b = "74",  5,  1
        Output= "24"
        self.assertEqual(Output, get_sol().findLexSmallestString(s,a,b))
    def test_3(self):
        s,a,b = "0011",  4,  2
        Output= "0011"
        self.assertEqual(Output, get_sol().findLexSmallestString(s,a,b))
    def test_4(self):
        s,a,b = "43987654",  7,  3
        Output= "00553311"
        self.assertEqual(Output, get_sol().findLexSmallestString(s,a,b))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):