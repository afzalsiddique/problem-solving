import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/smallest-string-with-swaps/discuss/387524/Short-Python-Union-find-solution-w-Explanation
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        root=list(range(n))

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]

        def union(x,y):
            root[find(x)] = root[find(y)]

        for x,y in pairs:
            union(x,y)

        di = defaultdict(list)
        for i in range(n):
            di[find(i)].append(s[i])

        for comp_id in di:
            di[comp_id].sort(reverse=True)

        res = []
        for i in range(n):
            res.append(di[find(i)].pop())
        return ''.join(res)


class Solution2:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        root = {} # also works
        def find(x):
            p=root.get(x,x)
            if p==x: return p
            root[x] = find(p)
            return root[x]
        def union(x,y):
            root[find(x)]=find(y)

        def sort_help(key):
            indices = di[key]
            tmp = [str(s[idx]) for idx in indices ]
            tmp.sort()
            for tmp_i in range(len(tmp)):
                s_i=indices[tmp_i]
                s[s_i]=tmp[tmp_i]

        s=list(s)
        for x,y in pairs: union(x,y)
        di = defaultdict(list)
        for i in range(len(s)):
            di[find(i)].append(i)

        for key in di:
            sort_help(key)
        return ''.join(s)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        expected = "bacd"
        actual = get_sol().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]])
        self.assertEqual(expected, actual)
    def test_2(self):
        expected = "abcd"
        actual = get_sol().smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]])
        self.assertEqual(expected, actual)
    def test_3(self):
        expected = "abc"
        actual = get_sol().smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]])
        self.assertEqual(expected, actual)

