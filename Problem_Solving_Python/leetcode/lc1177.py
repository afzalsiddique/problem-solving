import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def query(l,r,k):
            cnt=0
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                idx=ord(ch)-ord('a')
                cnt += (counts[idx][r+1]-counts[idx][l])%2
            return cnt//2 <= k

        counts=[]
        for ch1 in 'abcdefghijklmnopqrstuvwxyz':
            tmp=[0]
            for ch2 in s:
                tmp.append(tmp[-1]+1) if ch1==ch2 else tmp.append(tmp[-1])
            counts.append(tmp)

        return [query(l,r,k) for l,r,k in queries]

class Tester(unittest.TestCase):
    def test_1(self):
        s = "abcda"
        queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
        Output= [True,False,False,True,True]
        self.assertEqual(Output,get_sol().canMakePaliQueries(s,queries))
    # def test_2(self):
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):