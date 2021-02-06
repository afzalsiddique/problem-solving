import unittest
from leetcode.lc130 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        board = [["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
                ]
        expected = [["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
                ]
        solution.solve(board)
        self.assertEqual(expected, board)

    def test_2(self):
        solution = Solution()
        board = [["O","O"],["O","O"]]
        expected = [["O","O"],["O","O"]]
        solution.solve(board)
        self.assertEqual(expected, board)

    def test_3(self):
        solution = Solution()
        board = [["X", "X", "X", "X"],
                ["O", "O", "O", "O"],
                ["X", "X", "O", "X"],
                ["X", "X", "X", "X"],
                ]
        expected = [["X", "X", "X", "X"],
                ["O", "O", "O", "O"],
                ["X", "X", "O", "X"],
                ["X", "X", "X", "X"],
                ]
        solution.solve(board)
        self.assertEqual(expected, board)

    def test_4(self):
        solution = Solution()
        board = [["O"]]
        expected = [["O"]]
        solution.solve(board)
        self.assertEqual(expected, board)

    def test_5(self):
        solution = Solution()
        board = [["O","O"]]
        expected = [["O","O"]]
        solution.solve(board)
        self.assertEqual(expected, board)

    def test_6(self):
        solution = Solution()
        board = [["O","X"]]
        expected = [["O","X"]]
        solution.solve(board)
        self.assertEqual(expected, board)