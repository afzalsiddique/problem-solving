import unittest
from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = {}

        def add(x):
            if x not in parent:
                parent[x] = x

        def find(x):
            if x in parent:
                p = parent[x]
            else:
                p = x
            if p==x:
                return p

            parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            add(x),add(y)
            px,py = find(x), find(y)
            if px!=py:
                parent[px] = py

        n= len(isConnected)

        for i in range(n):
            add(i)

        for i in range(n):
            for j in range(n):
                if i==j:continue
                if isConnected[i][j]==1:
                    union(i,j)
        s = set()
        for temp_par in parent.values():
            true_parent = find(temp_par) # true_parent cannot be found until we call find function
            s.add(true_parent)
        return len(s)

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 2
        actual = sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 3
        actual = sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 1
        actual = sol.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.findCircleNum(0)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.findCircleNum(0)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.findCircleNum(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.findCircleNum(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.findCircleNum(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.findCircleNum(0)
        self.assertEqual(expected, actual)