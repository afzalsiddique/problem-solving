from collections import defaultdict;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], time: int, target: int) -> float:
        def dfs(u, par,time):
            if time<0: return 0
            if u==target:
                if time==0: return 1
                if u!=1 and len(g[u])==1: return 1
                return 0
            res=0
            for v in g[u]:
                if v==par: continue
                tmp=dfs(v,u,time-1)
                if tmp>0:
                    if u!=1:
                        tmp*=1/(len(g[u])-1)
                    else:
                        tmp*=1/(len(g[u]))
                    res+=tmp
            return res
        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        if len(edges)==0: return 1.0
        return dfs(1, -1, time)


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(0.16666666666666667, get_sol().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
    def test2(self):
        self.assertEqual(0.3333333333333333, get_sol().frogPosition( 7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1,  7))
    def test3(self):
        self.assertEqual(0.0, get_sol().frogPosition(6, [[2,1],[4,1],[5,1],[3,1],[6,3]], 7, 3))
    def test4(self):
        self.assertEqual(1.0, get_sol().frogPosition(1, [], 1, 1))
    def test5(self):
        self.assertEqual(0.0, get_sol().frogPosition(9, [[2,1],[3,2],[4,3],[5,3],[6,5],[7,3],[8,4],[9,5]], 9, 1))
    def test6(self):
        self.assertEqual(0.0, get_sol().frogPosition(5, [[2,1],[3,2],[5,3],[4,5]], 4, 1))
    def test7(self):
        self.assertEqual(0.16666666666666667, get_sol().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))
    def test8(self):
        self.assertEqual(0.0, get_sol().frogPosition(9, [[2,1],[3,1],[4,2],[5,3],[6,5],[7,4],[8,7],[9,7]], 1, 8))
    # def test9(self):
