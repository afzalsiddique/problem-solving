import unittest;
import functools


def get_sol(): return Solution()
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD=10**9+7
        dp=[[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            dp[i][0]=1
            for j in range(1,k+1):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
                dp[i][j]%=MOD
                if j-i>=0: # use sliding window technique to subtract
                    dp[i][j] = (dp[i][j]-dp[i-1][j-i])%MOD
        return dp[-1][-1]
class Solution2:
    # https://www.youtube.com/watch?v=XA4S-qTRsL0
    # tle
    def kInversePairs(self, n: int, k: int) -> int:
        MOD=10**9+7
        dp=[[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(i):
                for m in range(k+1):
                    if 0 <= m - j <= k:
                        dp[i][m] += dp[i-1][m-j]
                        dp[i][m] %= MOD
        return dp[-1][-1]
class Solution3:
    # tle
    def kInversePairs(self, n: int, k: int) -> int:
        MOD=10**9+7
        @functools.lru_cache(None)
        def recur(n,k):
            if n==0: return 0
            if k==0: return 1
            res=0
            for i in range(min(n-1,k)+1):
                res+=recur(n-1,k-i)
                res%=MOD
            return res

        return recur(n,k)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().kInversePairs(3,0))
    def test02(self):
        self.assertEqual(2,get_sol().kInversePairs(3,1))
    def test03(self):
        self.assertEqual(0,get_sol().kInversePairs(2,2))
    def test04(self):
        self.assertEqual(2,get_sol().kInversePairs(1000, 1000))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
