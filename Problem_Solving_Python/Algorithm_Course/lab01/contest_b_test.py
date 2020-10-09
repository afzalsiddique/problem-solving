import unittest
from Algorithm_Course.lab01.contest_b import *

class MyTestCase(unittest.TestCase):
    def test_2(self):
        n = 4
        dp = [[-1] * n for _ in range(n)]
        triangle = [
            [1],
            [1, 2],
            [4, 1, 2],
            [2, 3, 1, 1]
        ]
        expected = 9
        actual = f(triangle, n, dp, 0, 0)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
