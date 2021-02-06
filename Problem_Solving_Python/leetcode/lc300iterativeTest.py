import unittest
from leetcode.lc300iterative import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(4, solution.lengthOfLIS([10,9,2,5,3,7,101,18]))

    def test_2(self):
        solution = Solution()
        self.assertEqual(4, solution.lengthOfLIS([0,1,0,3,2,3]))

    def test_3(self):
        solution = Solution()
        self.assertEqual(1, solution.lengthOfLIS([7,7,7,7,7,7,7]))

    def test_4(self):
        solution = Solution()
        self.assertEqual(6, solution.lengthOfLIS([1,3,6,7,9,4,10,5,6]))