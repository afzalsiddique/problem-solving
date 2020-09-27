import unittest

from Leetcode743NetworkDelayTime.Solution import Solution


class MyTestCase(unittest.TestCase):
    def test_network(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        N = 4
        K = 2
        solution = Solution()
        actual = solution.networkDelayTime(times,N,K)
        expected = 2
        self.assertEqual(expected,actual)
