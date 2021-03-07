import unittest


class Solution:
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1


class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        actual = solution.mySqrt(9)
        expected = 3
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        actual = solution.mySqrt(10)
        expected = 3
        self.assertEqual(expected, actual)
    def test_3(self):
        solution = Solution()
        actual = solution.mySqrt(4)
        expected = 2
        self.assertEqual(expected, actual)
    def test_4(self):
        solution = Solution()
        actual = solution.mySqrt(8)
        expected = 2
        self.assertEqual(expected, actual)
    def test_5(self):
        solution = Solution()
        actual = solution.mySqrt(0)
        expected = 0
        self.assertEqual(expected, actual)
    def test_6(self):
        solution = Solution()
        actual = solution.mySqrt(1)
        expected = 1
        self.assertEqual(expected, actual)
