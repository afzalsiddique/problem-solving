import unittest
from leetcode.lc79 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = 'SEE'
        actual = solution.exist(word, board)
        expected = True
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCCED"
        actual = solution.exist(word, board)
        expected = True
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        word = "ABCB"
        actual = solution.exist(word, board)
        expected = False
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        board = [["A", "B", "C"], ["S", "F", "C"], ["A", "D", "E"]]
        word = "ABFD"
        actual = solution.exist(word, board)
        expected = True
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        board = [["A"]]
        word = "A"
        actual = solution.exist(word, board)
        expected = True
        self.assertEqual(expected, actual)

    def test_6(self):
        solution = Solution()
        board = [["a"]]
        word = "ab"
        actual = solution.exist(word, board)
        expected = False
        self.assertEqual(expected, actual)