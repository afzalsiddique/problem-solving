import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(i:int,j:int,pi:int,pj:int,vis:set[tuple]):
            if (i,j) in vis:
                return True
            vis.add((i,j))
            for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                newI,newJ=i+di,j+dj
                if not 0<=newI<m or not 0<=newJ<n:
                    continue
                if newI==pi and newJ==pj:
                    continue
                if grid[i][j]!=grid[newI][newJ]:
                    continue
                if dfs(newI,newJ,i,j,vis):
                    return True
            return False

        m,n=len(grid),len(grid[0])
        vis=set()
        for i in range(m):
            for j in range(n):
                if (i,j) not in vis:
                    if dfs(i,j,-1,-1,vis):
                        return True
        return False


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, get_sol().containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
    def test2(self):
        self.assertEqual(True, get_sol().containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))
    def test3(self):
        self.assertEqual(False, get_sol().containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
