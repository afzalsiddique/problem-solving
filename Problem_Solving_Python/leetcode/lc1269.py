import unittest;
import functools


def get_sol(): return Solution()
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD=10**9+7
        @functools.lru_cache(None)
        def dp(pos:int,steps:int):
            if not 0<=pos<arrLen: return 0
            if steps==0: return pos==0
            ans=0
            for dx in [-1,0,1]:
                ans+=dp(pos+dx,steps-1)
                ans%=MOD
            return ans

        return dp(0,steps)


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4,get_sol().numWays(steps = 3, arrLen = 2))
    def test_2(self):
        self.assertEqual(2,get_sol().numWays(steps = 2, arrLen = 4))
    def test_3(self):
        self.assertEqual(8,get_sol().numWays(steps = 4, arrLen = 2))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
