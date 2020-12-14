import unittest
from leetcode.lc90 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.subsetsWithDup([1,2,2]))
        expected = sorted([
                          [2],
                          [1],
                          [1,2,2],
                          [2,2],
                          [1,2],
                          []
                        ])
        self.assertEqual(expected, actual)
