import unittest
from leetcode.lc797 import *


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        graph = [[1, 2], [3], [3], []]
        actual = solution.allPathsSourceTarget(graph)
        expected = [[0,1,3],[0,2,3]]
        self.assertEqual(expected, actual)