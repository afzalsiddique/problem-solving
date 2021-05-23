import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def possible(word):
            func=defaultdict(set)
            inverse_func = defaultdict(set)
            if len(word)!=len(pattern): return False
            for c1,c2 in zip(word,pattern):
                func[c1].add(c2)
                inverse_func[c2].add(c1)
                if len(func[c1])>1: return False
                if len(inverse_func[c2])>1: return False
            return True

        res=[]
        for word in words:
            if possible(word):
                res.append(word)
        return res


class tester(unittest.TestCase):
    def test01(self):
        words = ["abc","deq","mee","aqq","dkd","ccc"]
        pattern = "abb"
        Output= ["mee","aqq"]
        self.assertEqual(Output, get_sol().findAndReplacePattern(words,pattern))
    def test02(self):
        words = ["a","b","c"]
        pattern = "a"
        Output= ["a","b","c"]
        self.assertEqual(Output, get_sol().findAndReplacePattern(words,pattern))
