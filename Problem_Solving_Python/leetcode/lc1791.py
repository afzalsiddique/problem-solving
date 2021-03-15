import unittest
from collections import defaultdict
from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        di = defaultdict(set)
        for u,v in edges:
            di[u].add(v)
            di[v].add(u)
        node,maxx=float('-inf'),float('-inf')

        for key in di:
            if len(di[key])>maxx:
                maxx=len(di[key])
                node=key
        return node

class MyTestCase(unittest.TestCase):

    def test_1(self):
        actual =Solution().findCenter([[1,2],[2,3],[4,2]])
        expected = 2
        self.assertEqual(expected, actual)
    def test_2(self):
        actual =Solution().findCenter([[1,2],[5,1],[1,3],[1,4]])
        expected = 1
        self.assertEqual(expected, actual)
