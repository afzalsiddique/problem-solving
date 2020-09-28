import unittest

from leetcode1462CourseScheduleIV.leetcode1462 import *


class MyTestCase(unittest.TestCase):
    def test_neighbor(self):
        n = 2
        prerequisites = [[1, 0]]
        queries = [[0, 1], [1, 0]]
        solution = Solution()
        actual = solution.checkIfPrerequisite(n, prerequisites, queries)
        expected = [False, True]
        self.assertEqual(expected,actual)
    def test_neighbor5(self):
        n = 5
        prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4]]
        queries = [[0, 4], [4, 0], [1, 3], [3, 0]]
        solution = Solution()
        actual = solution.checkIfPrerequisite(n, prerequisites, queries)
        expected = [True,False,True,False]
        self.assertEqual(expected,actual)