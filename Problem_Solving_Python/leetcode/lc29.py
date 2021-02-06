# https://www.youtube.com/watch?v=htX69j1jf5U
import unittest
from typing import List


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        def helper(dividend, divisor):
            if dividend<0 and divisor<0:
                return helper(-dividend, -divisor)
            if dividend<0 and divisor>0:
                quotient, dividend = helper(-dividend, divisor)
                return -quotient, dividend
            if dividend>0 and divisor<0:
                quotient, dividend = helper(dividend, -divisor)
                return -quotient, dividend

            if dividend<divisor:
                return 0, dividend
            else:
                dividend -= divisor
                quotient = 1
                temp, new_dividend = helper(dividend, 2*divisor)
                quotient += 2 * temp
                if new_dividend>=divisor:
                    new_dividend-=divisor
                    quotient+=1
            return quotient, new_dividend
        quotient = helper(dividend, divisor)[0]
        return min(max(-2147483648, quotient), 2147483647) # make sure that -2147483648 <= quotient <= 2147483647.

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = 3
        actual = sol.divide(dividend = 10, divisor = 3)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 2
        actual = sol.divide(dividend = 7, divisor = 3)
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 11
        actual = sol.divide(35, 3)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = -2
        actual = sol.divide(dividend = 7, divisor = -3)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 0
        actual = sol.divide(dividend = 0, divisor = 1)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 1
        actual = sol.divide(dividend = 1, divisor = 1)
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = -2147483648
        actual = sol.divide(-2147483648, 1)
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 4
        actual = sol.divide(4, 1)
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 4
        actual = sol.divide(8,2)
        self.assertEqual(expected, actual)

    def test_10(self):
        sol = Solution()
        expected = 2147483647
        actual = sol.divide(-2147483648, -1)
        self.assertEqual(expected, actual)