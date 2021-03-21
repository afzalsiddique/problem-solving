# https://leetcode.com/problems/string-to-integer-atoi/discuss/4643/Java-Solution-with-4-steps-explanations/145893
import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        index,total,sign,n =0,0,1,len(s)
        MAX_VALUE,MIN_VALUE = 2147483647, -2147483648

        if n==0:return 0

        while index<n and s[index]==' ':
            index+=1

        if index==n:return 0

        if s[index]=='+' or s[index]=='-':
            sign = 1 if s[index]=='+' else -1
            index+=1

        while index<n:
            digit = ord(s[index]) - ord('0')
            if digit < 0 or digit>9:break

            total = total * 10 + digit
            index+=1

            if sign == 1 and total>=MAX_VALUE:return MAX_VALUE
            if sign == -1 and total>=MAX_VALUE+1: return MIN_VALUE
        return total * sign


class Case(unittest.TestCase):
    def test_1(self):
        self.assertEqual(42,Solution().myAtoi('42'))
    def test_2(self):
        self.assertEqual(-42,Solution().myAtoi('-42'))
    def test_3(self):
        self.assertEqual(4193,Solution().myAtoi("4193 with words"))
    def test_4(self):
        self.assertEqual(0,Solution().myAtoi("words and 987"))
    def test_5(self):
        self.assertEqual(-2147483648,Solution().myAtoi("-91283472332"))
    def test_6(self):
        self.assertEqual(0,Solution().myAtoi("+-12"))
    def test_7(self):
        self.assertEqual(0,Solution().myAtoi("00000-42a1234"))
    def test_8(self):
        self.assertEqual(0,Solution().myAtoi("   +0 123"))
    def test_9(self):
        self.assertEqual(2147483646,Solution().myAtoi("2147483646"))
    def test_10(self):
        self.assertEqual(2147483647,Solution().myAtoi("2147483648"))
    def test_11(self):
        self.assertEqual(0,Solution().myAtoi(""))
    def test_12(self):
        self.assertEqual(0,Solution().myAtoi(" "))
