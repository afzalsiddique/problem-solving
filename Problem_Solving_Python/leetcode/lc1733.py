import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # for every 'lang' in languages:
    #   for two friends:
    #       if they don't speak the any common language
    #           we need to teach them speaking 'lang'
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        res=len(friendships)
        for lang in range(1,n+1):
            teach=set()
            for u,v in friendships:
                u-=1
                v-=1
                if languages[u] & languages[v]: continue
                if lang not in languages[u]: teach.add(u)
                if lang not in languages[v]: teach.add(v)
            res=min(res,len(teach))

        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        n,languages,friendships = 2,  [[1],[2],[1,2]],  [[1,2],[1,3],[2,3]]
        Output= 1
        self.assertEqual(Output, get_sol().minimumTeachings(n,languages,friendships))
    def test2(self):
        n,languages,friendships = 3,  [[2],[1,3],[1,2],[3]],  [[1,4],[1,2],[3,4],[2,3]]
        Output= 2
        self.assertEqual(Output, get_sol().minimumTeachings(n,languages,friendships))
    def test3(self):
        n,languages,friendships = 2,  [[1],[1],[1]],  [[1,2],[1,3],[2,3]]
        Output= 0
        self.assertEqual(Output, get_sol().minimumTeachings(n,languages,friendships))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
