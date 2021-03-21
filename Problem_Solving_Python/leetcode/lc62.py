import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def dfs(i, j):
            if i>=m or j>=n or i<0 or j<0:
                return 0
            if (i, j) in dp:return dp[(i, j)]
            if i==0 and j==0:return 1
            ans = dfs(i-1,j)+dfs(i,j-1)
            dp[(i,j)]=ans
            return dp[(i,j)]
        return dfs(m-1,n-1)

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==1 and n==1:
            return 1
        dp = [[1]*n for _ in range(m)] # first row and first col 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        m,n=3,7
        actual = solution.uniquePaths(m,n)
        expected = 28
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        m,n=7,3
        actual = solution.uniquePaths(m,n)
        expected = 28
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        m,n=3,2
        actual = solution.uniquePaths(m,n)
        expected = 3
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        m,n=3,3
        actual = solution.uniquePaths(m,n)
        expected = 6
        self.assertEqual(expected, actual)