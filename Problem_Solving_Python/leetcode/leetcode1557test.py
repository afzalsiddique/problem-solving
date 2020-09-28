import unittest


from leetcode.leetcode1557 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        n = 6
        edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
        solution = Solution()
        actual = solution.findSmallestSetOfVertices(n, edges)
        expected = [0, 3]
        self.assertEqual(expected, actual)

    def test_2(self):
        n = 5
        edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
        solution = Solution()
        actual = solution.findSmallestSetOfVertices(n, edges)
        expected = [0, 2, 3]
        self.assertEqual(expected, actual)