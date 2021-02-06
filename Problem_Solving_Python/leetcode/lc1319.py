import unittest
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        roots = {}
        def add(x):
            if x not in roots:
                roots[x] = x
        def find(x):
            if x in roots:
                p = roots[x]
            else:
                p = x
            if p==x:
                return p
            roots[x] = find(roots[x])
            return roots[x]

        def union(x,y):
            add(x), add(y)
            px, py = find(x), find(y)
            if px!=py:
                roots[px] = roots[py]

        for i in range(n):
            add(i)

        for x,y in connections:
            union(x,y)

        s = set()
        for temp_parent in roots:
            true_parent = find(temp_parent)
            s.add(true_parent)
        cables_required = len(s) - 1
        return cables_required if (len(connections)) >= (n-1) else -1



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 1
        actual = sol.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 2
        actual = sol.makeConnected( n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = -1
        actual = sol.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.makeConnected( n = 5, connections = [[0,1],[0,2],[3,4],[2,3]])
        self.assertEqual(expected, actual)

