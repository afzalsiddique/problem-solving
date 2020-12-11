import unittest
from leetcode.lc96 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        n = 1
        actual = solution.numTrees(n)
        expected = 1
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        n = 2
        actual = solution.numTrees(n)
        expected = 2
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        n = 3
        actual = solution.numTrees(n)
        expected = 5
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        n = 4
        actual = solution.numTrees(n)
        expected = 14
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()


