import unittest
from leetcode.leetcode169 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [3,2,3]
        actual = solution.majorityElement(nums)
        expected = 3
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2]
        actual = solution.majorityElement(nums)
        expected = 2
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [6,5,5]
        actual = solution.majorityElement(nums)
        expected = 5
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
