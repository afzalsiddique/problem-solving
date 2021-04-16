# https://www.youtube.com/watch?v=CMaZ69P1bAc
import unittest


class Solution:
    # recursive dp
    def numTrees(self, n: int) -> int:
        dp = {}
        def catalan(n):
            if n==0 or n==1: return 1
            if n in dp: return dp[n]
            ans =0
            for i in range(n):
                ans+=catalan(i)*catalan(n-i-1)
            dp[n]=ans
            return dp[n]
        return catalan(n)
    # iterative dp
    def numTrees2(self, n: int) -> int:
        def catalan(nth):
            dp = [0]*(nth+1)
            dp[0] = dp[1] = 1
            if nth == 0 or nth == 1: return 1
            for n in range(2, nth + 1):
                for i in range(n):
                    dp[n] += dp[i] * dp[n-i-1]
            return dp[nth]

        return catalan(n)

    # binomial coefficient
    def numTrees3(self, n: int) -> int:
        di={}
        def factorial(n):
            if n==0 or n==1: return 1
            if n in di: return di[n]
            di[n]=n*factorial(n-1)
            return di[n]

        def catalan(n):
            return factorial(2*n) / factorial(n) / factorial(n+1)

        return int(catalan(n))

class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        n = 1
        actual = solution.numTrees(n)
        expected = 1
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        n = 2
        actual = solution.numTrees(n)
        expected = 2
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        n = 3
        actual = solution.numTrees(n)
        expected = 5
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        n = 4
        actual = solution.numTrees(n)
        expected = 14
        self.assertEqual(expected, actual)
