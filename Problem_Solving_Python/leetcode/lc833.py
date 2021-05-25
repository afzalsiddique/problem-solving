import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def findReplaceString(self, s: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        li=list(s)
        def replace(i, source, target):
            if source== s[i:i + len(source)]:
                for i in range(i, i + len(source)):
                    li[i]=""
                li[i]=target

        for i,source,target in zip(indexes,sources,targets):
            replace(i,source,target)
        return ''.join(li)
class tester(unittest.TestCase):
    def test01(self):
        s = "abcd"
        indexes = [0, 2]
        sources = ["a", "cd"]
        targets = ["eee", "ffff"]
        Output= "eeebffff"
        self.assertEqual(Output, get_sol().findReplaceString(s, indexes, sources, targets))
    def test02(self):
        s = "abcd"
        indexes = [0, 2]
        sources = ["ab","ec"]
        targets = ["eee","ffff"]
        Output= "eeecd"
        self.assertEqual(Output, get_sol().findReplaceString(s, indexes, sources, targets))