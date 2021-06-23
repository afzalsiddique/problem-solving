import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # similar to 46
    def numTilePossibilities(self, tiles: str) -> int:
        res=set()
        def helper(strs,path):
            if ''.join(path) in res: return # optimization
            if path: res.add(''.join(path))
            for i in range(len(strs)):
                helper(strs[:i]+strs[i+1:],path+[strs[i]])
        helper(tiles,[])
        return len(res)

class Solution2:
    # similar to 47
    def numTilePossibilities(self, tiles: str) -> int:
        res=[]
        def helper(strs,path):
            if path: res.append(''.join(path))
            for i in range(len(strs)):
                if i>0 and strs[i]==strs[i-1]: continue
                helper(strs[:i]+strs[i+1:],path+[strs[i]])

        tiles = list(tiles)
        tiles.sort()
        helper(tiles,[])
        return len(res)

class tester(unittest.TestCase):
    def test_01(self):
        tiles = "AAB"
        Output= 8
        self.assertEqual(Output,get_sol().numTilePossibilities(tiles))
    def test_02(self):
        tiles = "AAABBC"
        Output= 188
        self.assertEqual(Output,get_sol().numTilePossibilities(tiles))
    def test_03(self):
        tiles = "V"
        Output= 1
        self.assertEqual(Output,get_sol().numTilePossibilities(tiles))
