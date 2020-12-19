import unittest
from leetcode.lc113 import *


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        nodes = [5,4,8,11,-1,13,4,7,2,-1,-1,-1,1]
        sum = 22
        actual = solution.pathSum(nodes, sum)
        expected = [[5,4,11,2], [5,8,4,5]]
        self.assertEqual(expected, actual)