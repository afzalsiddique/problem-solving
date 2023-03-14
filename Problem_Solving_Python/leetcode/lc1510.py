import math;
import unittest;
import functools


def get_sol(): return Solution()
class Solution:
    # Think about this problem from alice perspective.
    # If we can find an idx where Alice loses and idx<i, then we can flip the result
    def winnerSquareGame(self, n: int) -> bool:
        dp=[False]*(n+1)
        for i in range(1,n+1):
            sqroot=int(math.sqrt(n))
            for j in range(1,sqroot+1):
                idx=i-j*j
                if idx<0: break
                if dp[idx]==False:
                    dp[i]=True
                    break
        return dp[-1]
class Solution2:
    # tle. minimax
    def winnerSquareGame(self, n: int) -> bool:
        def get_squares(n):
            return [i*i for i in range(1,int(math.sqrt(n))+1)]

        @functools.lru_cache(None)
        def minimax(n,player):
            if n==0: return not player
            res=not player
            if player:
                for i in get_squares(n):
                    res=max(res,minimax(n-i,not player))
            else:
                for i in get_squares(n):
                    res=min(res,minimax(n-i,not player))
            return res

        return minimax(n,True)



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(True, get_sol().winnerSquareGame(1))
    def test02(self):
        self.assertEqual(False, get_sol().winnerSquareGame(2))
    def test03(self):
        self.assertEqual(True, get_sol().winnerSquareGame(3))
    def test04(self):
        self.assertEqual(True, get_sol().winnerSquareGame(4))
    def test05(self):
        self.assertEqual(False, get_sol().winnerSquareGame(5))
    def test06(self):
        self.assertEqual(True, get_sol().winnerSquareGame(6))
    def test07(self):
        self.assertEqual(False, get_sol().winnerSquareGame(7))
    def test08(self):
        self.assertEqual(True, get_sol().winnerSquareGame(8))
    def test09(self):
        self.assertEqual(True, get_sol().winnerSquareGame(9))
    def test10(self):
        self.assertEqual(False, get_sol().winnerSquareGame(10))
    def test11(self):
        self.assertEqual(True, get_sol().winnerSquareGame(92719))

