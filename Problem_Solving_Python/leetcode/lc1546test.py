import unittest
from leetcode.lc1546 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        nums = [-1, 3, 5, 1, 4, 2, -9]
        target = 6
        actual = solution.maxNonOverlapping(nums, target)
        expected = 2
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [1,1,1,1,1]
        target = 2
        actual = solution.maxNonOverlapping(nums, target)
        expected = 2
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()


