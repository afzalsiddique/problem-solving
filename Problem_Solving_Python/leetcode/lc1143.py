import unittest


class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        # https://www.youtube.com/watch?v=sSno9rV8Rhg&t=305s
        m,n= len(a), len(b)
        di = {}
        def helper(i,j):
            if i==m or j==n:
                return 0
            if (i,j) in di:
                return di[(i,j)]
            if a[i]==b[j]:
                di[(i,j)] = 1+helper(i+1,j+1)
                return di[(i,j)]
            else:
                di[(i,j)]= max(helper(i+1,j),helper(i,j+1))
                return di[(i,j)]

        return helper(0,0)

    def longestCommonSubsequence_(self, a: str, b: str) -> int:
        m,n=len(a),len(b)
        di = {}
        def helper(i,j):
            if i<0 or j<0:
                return 0
            if (i,j) in di:
                return di[(i,j)]
            if a[i]==b[j]:
                di[(i,j)] = 1 + helper(i-1,j-1)
                return di[(i,j)]
            else:
                di[(i,j)] = max(helper(i-1,j),helper(i,j-1))
                return di[(i,j)]
        return helper(m-1,n-1)
    def longestCommonSubsequence__(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]

class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        text1 = 'abcdefg'
        text2 = 'chfg'
        actual = solution.longestCommonSubsequence(text1, text2)
        expected = 3
        self.assertEqual(expected, actual)


    def test_2(self):
        solution = Solution()
        text1 = 'abcde'
        text2 = 'ace'
        actual = solution.longestCommonSubsequence(text1, text2)
        expected = 3
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        text1 = "oxcpqrsvwf"
        text2 = "shmtulqrypy"
        actual = solution.longestCommonSubsequence(text1, text2)
        expected = 2
        self.assertEqual(expected, actual)
