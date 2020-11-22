import unittest
from leetcode.leetcode215 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [3,2,1,5,6,4]
        k = 2
        actual = solution.findKthLargest(nums, k)
        expected = 5
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        actual = solution.findKthLargest(nums, k)
        expected = 4
        self.assertEqual(expected, actual)






if __name__ == '__main__':
    unittest.main()
