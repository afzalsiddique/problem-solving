import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s:str):
            count = Counter(s)
            for c in string.ascii_lowercase:
                if count[c]:
                    return count[c]

        queries = [f(s) for s in queries]
        words = [f(s) for s in words]
        words.sort()
        res = []
        for q in queries:
            idx = bisect_right(words, q)
            res.append(len(words)-idx)
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        queries, words = ["cbd"], ["zaaaz"]
        Output= [1]
        self.assertEqual(Output, get_sol().numSmallerByFrequency(queries, words))
    def test2(self):
        queries, words = ["bbb","cc"], ["a","aa","aaa","aaaa"]
        Output= [1,2]
        self.assertEqual(Output, get_sol().numSmallerByFrequency(queries, words))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
