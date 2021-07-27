import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/pyramid-transition-matrix/discuss/113038/Python-Solution/470281
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def dfs(i, base, path):
            if len(base)==1: return True
            if len(path)==len(base)-1: # if i==len(base)-1: # works as well
                return dfs(0,path,'')
            tmp= base[i:i+2]
            for s in di[tmp]:
                if dfs(i+1, base, path+s):
                    return True
            return False

        di=defaultdict(list)
        for x in allowed:
            di[x[:2]].append(x[2])

        return dfs(0,bottom,'')

class tester(unittest.TestCase):
    def test_1(self):
        bottom = "BCD"
        allowed = ["BCG","CDE","GEA","FFF"]
        Output= True
        self.assertEqual(Output, get_sol().pyramidTransition(bottom,allowed))
    def test_2(self):
        bottom = "AABA"
        allowed = ["AAA","AAB","ABA","ABB","BAC"]
        Output= False
        self.assertEqual(Output, get_sol().pyramidTransition(bottom,allowed))
    def test_3(self):
        bottom = "ABCD"
        allowed = ["BCE","BCF","ABA","CDA","AEG","FAG","GGG"]
        Output= False
        self.assertEqual(Output, get_sol().pyramidTransition(bottom,allowed))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
