import unittest
from leetcode.lc51 import *
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(4))
        expected = sorted([[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(5))
        expected = sorted([['....Q', '..Q..', 'Q....', '...Q.', '.Q...'],
                         ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'],
                         ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'],
                         ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'],
                         ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'],
                         ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'],
                         ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'],
                         ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'],
                         ['Q....', '...Q.', '.Q...', '....Q', '..Q..'],
                         ['Q....', '..Q..', '....Q', '.Q...', '...Q.']] )
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(3))
        expected = sorted([])
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(2))
        expected = sorted([])
        self.assertEqual(expected, actual)

    def test_5(self):
        solution = Solution()
        actual = sorted(solution.solveNQueens(1))
        expected = sorted([['Q']])
        self.assertEqual(expected, actual)

