import unittest
from Algorithm_Course.lab01.contest_a import *

class MyTestCase(unittest.TestCase):
    def test_bottom_index(self):
        i, j, n = 0, 0, 4
        expected = (1,0)
        actual = get_bottom1(i,j,n)
        self.assertEqual(expected, actual)


    # def test_1(self):
    #     N = 4
    #     k = 2*N -1
    #     a = [
    #         [7,0,0,0,0],
    #         [6,4,0,0,0],
    #         [2,5,10,0,0],
    #         [9,8,12,2,0],
    #         [0,2,12,7,0],
    #         [0,0,8,2,0],
    #         [0,0,0,10,0]
    #     ]
    #     dp = [[-1] * N for _ in range(k)]
    #     actual = calculate_bananas(a,dp, 0,0, k)
    #     expected = 63
    #     self.assertEqual(expected, actual)
    #
    # def test_2(self):
    #     N = 2
    #     k = 2*N -1
    #     a = [
    #         [1,0,0],
    #         [2,3,0],
    #         [0,1,0]
    #     ]
    #     dp = [[-1] * N for _ in range(k)]
    #     actual = calculate_bananas(a,dp, 0,0, k)
    #     expected = 5
    #     self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
