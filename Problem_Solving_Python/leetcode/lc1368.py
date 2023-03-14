import math;
from collections import deque, defaultdict;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    # 0-1 bfs shortest path binary graph
    # https://www.youtube.com/watch?v=cMP1IaWuFuM
    def minCost(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dir={1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
        min_cost = defaultdict(lambda: math.inf, {(0, 0): 0})
        q = deque([(0,0,0)]) # cost,i,j
        while q:
            cost,x,y=q.popleft()
            if x==m-1 and y==n-1: return cost
            for d in range(1,4+1):
                step_cost=0
                if d!=grid[x][y]:
                    step_cost+=1
                x2,y2=x+dir[d][0],y+dir[d][1]
                if not 0<=x2<m or not 0<=y2<n: continue
                cost2 = cost + step_cost
                if cost2 < min_cost[x2, y2]:
                    min_cost[x2, y2] = cost2
                    if not step_cost:
                        q.appendleft((cost2, x2, y2))
                    else:
                        q.append((cost2, x2, y2))


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
    def test2(self):
        self.assertEqual(0, get_sol().minCost([[1,1,3],[3,2,2],[1,1,4]]))
    def test3(self):
        self.assertEqual(1, get_sol().minCost([[1,2],[4,3]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):

