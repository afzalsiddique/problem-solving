from functools import cache;
import unittest;
import functools;


def get_sol(): return Solution()
class Solution:
    # pattern 121: 121, 131, 212, 232, 313, 323.
    # pattern 123: 123, 132, 213, 231, 312, 321.
    # Pattern 121 can be followed by: 212, 213, 232, 312, 313
    # Pattern 123 can be followed by: 212, 231, 312, 232
    # 121 => three 121, two 123
    # 123 => two 121, two 123
    def numOfWays(self, n: int) -> int:
        MOD=10**9+7
        a123=6
        a121 = 6
        for i in range(n-1):
            b123=2*a123+2*a121
            b121=3*a121+2*a123
            a121=b121%MOD
            a123=b123%MOD
        return (a123+a121)%MOD
class Solution2:
    def numOfWays(self, n: int) -> int:
        MOD=10**9+7
        @cache
        def dp(n, prevCol0, prevCol1, prevCol2):
            if n==0: return 1
            res=0
            li = [-1,-1,-1]
            for col0 in range(3):
                if col0==prevCol0: continue
                li[0]=col0
                for col1 in range(3):
                    if col0==col1: continue
                    if col1==prevCol1: continue
                    li[1]=col1
                    for col2 in range(3):
                        if col2==col1: continue
                        if col2==prevCol2: continue
                        li[2]=col2
                        res+=dp(n-1,li[0],li[1],li[2])
                        res%=MOD

            return res

        return dp(n,-3,-2,-1)
class Solution3:
    # tle
    def numOfWays(self, n: int) -> int:
        MOD=10**9+7
        def check(row):
            for x,y in zip(row, row[1:]):
                if x==y: return False
            return True
        def checkTwoRows(row1,row2):
            for x,y in zip(row1,row2):
                if x==y: return False
            return True
        @functools.lru_cache(None)
        def dp(n, prevRow):
            if n==0: return 1
            res=0
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        row = (i,j,k)
                        if check(row) and checkTwoRows(row,prevRow):
                            res+=dp(n-1,row)
                            res%=MOD
            return res

        return dp(n,(-3,-2,-1))

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(12, get_sol().numOfWays(1))
    def test2(self):
        self.assertEqual(30228214, get_sol().numOfWays(5000))
    def test3(self):
        self.assertEqual(61735875, get_sol().numOfWays(2727))
    def test4(self):
        self.assertEqual(54, get_sol().numOfWays(2))
    def test5(self):
        self.assertEqual(246, get_sol().numOfWays(3))
    # def test6(self):
    # def test7(self):

