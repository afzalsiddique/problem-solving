import unittest
from leetcode.leetcode241 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        str = "2*3-4"
        actual = sorted(solution.diffWaysToCompute(str))
        expected = [-2,2]
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        str = "2*3-4*5"
        actual = sorted(solution.diffWaysToCompute(str))
        expected = sorted([-34, -14, -10, -10, 10])
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
