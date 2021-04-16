# https://leetcode.com/problems/string-to-integer-atoi/discuss/4643/Java-Solution-with-4-steps-explanations/145893
import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s)==0:return 0
        ans,INT_MAX,INT_MIN = 0,2147483647,-2147483648
        sign = 1
        for i in range(len(s)):
            if s[i]!=' ':break
        if s[i]=='+' or s[i]=='-':
            sign = -1 if s[i]=='-' else 1
            i+=1
        i_copy = i
        for i in range(i_copy,len(s)):
            if s[i]<'0' or s[i]>'9':break
            digit = int(s[i])
            if ans > (INT_MAX-digit)//10:
                return INT_MAX if sign == 1 else INT_MIN
            ans = ans*10+digit
        return sign * ans


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
