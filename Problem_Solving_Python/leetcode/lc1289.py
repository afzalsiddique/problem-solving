import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dp=[[float('inf')]*n for _ in range(n)]
        for j in range(n):
            dp[0][j]=grid[0][j]
        for i in range(1,n):
            minn1,idx1=float('inf'),-1
            minn2=float('inf')
            for k in range(n):
                if dp[i-1][k]<minn1:
                    minn2=minn1
                    minn1=dp[i-1][k]
                    idx1=k
                elif dp[i-1][k]<minn2:
                    minn2=dp[i-1][k]
            for j in range(n):
                if j!=idx1:
                    dp[i][j]=grid[i][j]+minn1
                else:
                    dp[i][j]=grid[i][j]+minn2
        return min(dp[-1])
class Solution2:
    # tle
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        dp=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==0:
                    dp[i][j]=grid[i][j]
                else:
                    for k in range(n):
                        if j==k: continue
                        dp[i][j]=min(dp[i][j],grid[i][j]+dp[i-1][k])
        return min(dp[-1])
class Solution3:
    # tle
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def calculateSum(mask:tuple[int]):
            res=0
            for i in range(m):
                j=mask[i]
                res+=grid[i][j]
            return res
        def turnOn(mask:tuple[int],i:int, char:int):
            li = list(mask)
            li[i]=char
            return tuple(li)
        # @functools.lru_cache(None)
        def func(i: int, last: int, mask: tuple[int]):
            if i==m:
                summ=calculateSum(mask)
                return summ
            if mask in dp: return dp[mask]
            res=float('inf')
            for j in range(n):
                if j==last: continue
                res=min(res, func(i + 1, j, turnOn(mask, i, j)))
            dp[mask]=res
            return res

        m,n=len(grid),len(grid[0])
        dp={}
        res= func(0, -1, tuple(0 for _ in range(m)))
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(13, get_sol().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
    def test2(self):
        self.assertEqual(7, get_sol().minFallingPathSum([[7]]))
    def test3(self):
        self.assertEqual(-879, get_sol().minFallingPathSum([[-2,-18,31,-10,-71,82,47,56,-14,42],[-95,3,65,-7,64,75,-51,97,-66,-28],[36,3,-62,38,15,51,-58,-90,-23,-63],[58,-26,-42,-66,21,99,-94,-95,-90,89],[83,-66,-42,-45,43,85,51,-86,65,-39],[56,9,9,95,-56,-77,-2,20,78,17],[78,-13,-55,55,-7,43,-98,-89,38,90],[32,44,-47,81,-1,-55,-5,16,-81,17],[-87,82,2,86,-88,-58,-91,-79,44,-9],[-96,-14,-52,-8,12,38,84,77,-51,52]]))
    def test4(self):
        self.assertEqual(-231, get_sol().minFallingPathSum( [[4,30,14,38],[-52,-92,65,-85],[-3,-77,8,-19],[-71,-21,-62,-73]] ))
    def test5(self):
        self.assertEqual(-235, get_sol().minFallingPathSum( [[-92,65,-85],[-77,8,-19],[-21,-62,-73]] ))
    # def test6(self):
    # def test7(self):

