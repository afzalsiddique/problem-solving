# https://leetcode.com/problems/evaluate-division/discuss/278276/Java-Union-Find-and-DFS-Query-O(1)
import unittest
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        parents = {}
        vals = {}
        res = [0 for _ in range(len(queries))]

        def add(x):
            if x in parents: return
            parents[x] = x
            vals[x] = 1

        def find(x):
            if x in parents:
                p = parents[x]
            else:
                p = x

            if p != x:
                pp = find(p)
                vals[x] = vals[x] * vals[p]
                parents[x] = pp
            if x in parents:
                return parents[x]
            else:
                return x

        def union(x, y, value):
            add(x), add(y)
            px, py = find(x), find(y)
            parents[px] = py
            val,valsy,valsx = value, vals[y], vals[x]
            vals[px] = value * vals[y] / vals[x]

        for i in range(n):
            union(equations[i][0], equations[i][1], values[i])
        for i in range(len(queries)):
            x, y = queries[i][0], queries[i][1]
            if x in parents and y in parents and find(x) == find(y):
                res[i] = vals[x] / vals[y]
            else:
                res[i] = -1
        return res


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        actual = sol.calcEquation(equations=[["a", "b"], ["b", "c"]], values=[2.0, 3.0],
                                  queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 0
        actual = sol.calcEquation(equations=[["a", "b"], ["a", "c"],['d','e'],['e','f'],['b','e']], values=[2.0, 3.0,8,7,10,13],
                                  queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 0
        actual = sol.calcEquation(0)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.calcEquation(0)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.calcEquation(0)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.calcEquation(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.calcEquation(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.calcEquation(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.calcEquation(0)
        self.assertEqual(expected, actual)
