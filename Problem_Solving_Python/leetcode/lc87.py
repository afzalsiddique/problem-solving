import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        dp = {}
        def helper(s1:str,s2:str)-> bool:
            if s1==s2: return True
            if (s1,s2) in dp: return dp[s1,s2]
            if len(s1) != len(s2) or sorted(s1) != sorted(s2): # prunning
                dp[(s1, s2)] = False
                return False
            for i in range(1,len(s1)): # len(s1) is equal to len(s2)
                # print(1,s1[:i],s2[:i],s1[i:],s2[i:])
                # print(2,s1[:i],s2[-i:],s1[i:],s2[:-i])
                if helper(s1[:i],s2[:i]) and helper(s1[i:],s2[i:]) \
                        or helper(s1[:i],s2[-i:]) and helper(s1[i:],s2[:-i]): # swapping
                    dp[s1,s2]=True
                    return True
            dp[s1,s2]=False
            return False

        return helper(s1,s2)

class tester(unittest.TestCase):
    def test01(self):
        s1 = "great"
        s2 = "rgeat"
        Output= True
        self.assertEqual(Output,get_sol().isScramble(s1,s2))
    def test02(self):
        s1 = "abcde"
        s2 = "caebd"
        Output= False
        self.assertEqual(Output,get_sol().isScramble(s1,s2))
    def test03(self):
        s1 = "a"
        s2 = "a"
        Output= True
        self.assertEqual(Output,get_sol().isScramble(s1,s2))
    def test04(self):
        s1 = "abc"
        s2 = "bca"
        Output= True
        self.assertEqual(Output,get_sol().isScramble(s1,s2))

