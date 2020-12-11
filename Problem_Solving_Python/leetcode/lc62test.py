import unittest
from leetcode.lc62 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        m,n=3,7
        actual = solution.uniquePaths(m,n)
        expected = 28
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        m,n=7,3
        actual = solution.uniquePaths(m,n)
        expected = 28
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        m,n=3,2
        actual = solution.uniquePaths(m,n)
        expected = 3
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        m,n=3,3
        actual = solution.uniquePaths(m,n)
        expected = 6
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
