import unittest

from leetcode.leetcode743 import Solution


class MyTestCase(unittest.TestCase):
    def test_network(self):
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        N = 4
        K = 2
        solution = Solution()
        actual = solution.networkDelayTime(times, N, K)
        expected = 2
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
