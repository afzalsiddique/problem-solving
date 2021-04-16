import unittest


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def pali(s):
            n=len(s)
            if n==1:return 1
            if n==2:
                if s[0]==s[1]:return 2
                return 1
            if s in di:return di[s]
            if s[0]==s[-1]:
                di[s]= 2 + pali(s[1:-1])
            else:
                di[s] = max(pali(s[:-1]),pali(s[1:]))
            return di[s]


        di = {}
        return pali(s)


    def longestPalindromeSubseq_(self, s: str) -> int:
        n = len(s)
        dp = [[1] * n for _ in range(n)]
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 2
        for left in range(n - 1, -1, -1):
            for right in range(left + 2, n):
                if s[left] == s[right]:
                    dp[left][right] = dp[left + 1][right - 1] + 2
                else:
                    dp[left][right] = max(dp[left][right-1], dp[left+1][right])
        return dp[0][n-1]

    # to find actual palindrome (string)
    def longestPalindromeSubseq__(self, s: str) -> int:
        dp = {}
        def helper(s:str):
            n=len(s)
            if n==0:return ""
            if n==1:return s
            if n==2:
                if s[0]==s[1]:return s
                else:return s[0]
            if s in dp:return dp[s]
            if s[0]==s[-1]:
                return s[0] + helper(s[1:-1]) + s[-1]
            else:
                s1 = helper(s[:-1])
                s2 = helper(s[1:])
                if len(s1)>len(s2):
                    dp[s] = s1
                    return s1
                dp[s] = s2
                return s2

        return len(helper(s))


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        s = 'bbbab'
        expected = 4
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = 'cbbd'
        expected = 2
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = 'abcdef'
        expected = 1
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)
    def test_4(self):
        solution = Solution()
        s = 'bbb'
        expected = 3
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)
    def test_5(self):
        solution = Solution()
        s = 'bbbb'
        expected = 4
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)
    def test_6(self):
        solution = Solution()
        s = 'qwertbbbbzxcv'
        expected = 4
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)
    def test_7(self):
        solution = Solution()
        s = 'qAwAeAAtAyAu'
        expected = 6
        actual = solution.longestPalindromeSubseq(s)
        self.assertEqual(expected, actual)
