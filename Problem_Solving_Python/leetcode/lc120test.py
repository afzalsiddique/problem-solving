import unittest
from leetcode.lc120 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        triangle = [
                     [2],
                    [3,4],
                   [6,5,7],
                  [4,1,8,3]
                    ]
        actual = solution.minimumTotal(triangle)
        expected = 11
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        triangle = [
                     [2],
                    [3,4]
                    ]
        actual = solution.minimumTotal(triangle)
        expected = 5
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()


