import unittest
from leetcode.leetcode238 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [2,3,4,5]
        actual = solution.productExceptSelf(nums)
        expected = [60, 40, 30, 24]
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
