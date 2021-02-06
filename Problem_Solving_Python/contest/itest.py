import unittest

from contest.i import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        actual = sol.func()
        expected = 0
        self.assertEqual(expected, actual)