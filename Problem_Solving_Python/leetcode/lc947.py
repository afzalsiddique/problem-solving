import unittest
from typing import List


class Solution:
    # union find
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        root = {}

        def add(x):
            if x not in root:
                root[x] = x

        def find(x):
            if x in root:
                p = root[x]
            else:
                p = x
            if p==x:
                return p

            root[x] = find(p)
            return root[x]

        def union(x,y):
            add(x),add(y)
            px,py = find(x), find(y)
            if px!=py:
                root[px] = py

        for row, col in stones:
            union('r'+str(row),'c'+str(col))

        unique_root_set = set()
        for temp_root in root.values():
            true_root = find(temp_root)
            unique_root_set.add(true_root)

        return n-len(unique_root_set)

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 5
        actual = sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 3
        actual = sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 0
        actual = sol.removeStones([[0,0]])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 0
        actual = sol.removeStones(0)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.removeStones(0)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.removeStones(0)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 0
        actual = sol.removeStones(0)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 0
        actual = sol.removeStones(0)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 0
        actual = sol.removeStones(0)
        self.assertEqual(expected, actual)