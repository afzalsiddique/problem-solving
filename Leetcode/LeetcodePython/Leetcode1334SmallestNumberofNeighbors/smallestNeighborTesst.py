import unittest

from Leetcode1334SmallestNumberofNeighbors.leetcode1334 import *


class MyTestCase(unittest.TestCase):
    def test_neighbor(self):
        n = 4
        edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
        distanceThreshold = 4
        solution = Solution()
        actual = solution.findTheCity(n, edges, distanceThreshold)
        expected = 3
        self.assertEqual(expected,actual)

    def test_neighbor2(self):
        n = 5
        edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2],[2,3,1],[3,4,1]]
        distanceThreshold = 2
        solution = Solution()
        actual = solution.findTheCity(n, edges, distanceThreshold)
        expected = 0
        self.assertEqual(expected,actual)