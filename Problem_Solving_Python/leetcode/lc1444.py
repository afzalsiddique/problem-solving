import unittest; from typing import List; import functools


def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/discuss/623732/JavaC%2B%2BPython-DP-%2B-PrefixSum-in-Matrix-Clean-code
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9+7
        @functools.lru_cache(None)
        def dfs(r, c, k):
            if pre[r][c]==0: # does not contain apple
                return 0
            if k==0:
                return 1

            res=0
            # cut horizontally
            for i in range(r+1, m):
                if pre[r][c]-pre[i][c]>=1: # contains apple
                    res+=dfs(i, c, k-1)
                    res%=MOD

            # cut vertically
            for j in range(c+1, n):
                if pre[r][c]-pre[r][j]>=1: # contains apple
                    res+=dfs(r,j, k-1)
                    res%=MOD

            return res

        m,n=len(pizza),len(pizza[0])
        pre=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                pre[i][j]=pre[i+1][j]+pre[i][j+1]-pre[i+1][j+1]+(1 if pizza[i][j]=='A' else 0)

        return dfs(0,0,k-1)


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().ways(["A..","AAA","..."],  3))
    def test02(self):
        self.assertEqual(1, get_sol().ways(["A..","AA.","..."],  3))
    def test03(self):
        self.assertEqual(1, get_sol().ways(["A..","A..","..."], 1))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
