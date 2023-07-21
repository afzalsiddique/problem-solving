from collections import defaultdict;
import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # instead of undirected graph construct a directed graph
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        def dfs(u,t): # return probability
            if t==0 or len(g[u])==0:
                return 1 if u==target else 0

            prob=0
            for v in g[u]:
                prob=dfs(v,t-1)
                if prob: # if target is found among the children of the current node
                    break

            totalBranches=len(g[u])
            prob=prob*(1/totalBranches)
            return prob

        g={1:[]} # instead of undirected graph construct a directed graph
        for a,b in edges:
            if a not in g: a,b=b,a
            g[a].append(b)
            g[b]=[]
        return dfs(1,t)
class Solution3:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        def dfs(i,par,t): # return target/total
            if t==0:
                return int(i==target)
            totalBranches=len(g[i]) if i==1 else len(g[i])-1
            targetBranches=0
            for j in g[i]:
                if j==par: continue
                targetBranches+=dfs(j,i,t-1)
            if totalBranches!=0:
                return targetBranches/totalBranches
            # jumping in the same position indefinitely
            if i==target:
                return 1
            return 0

        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        return dfs(1,-1,t)
class Solution2:
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
    def test01(self):
        self.assertEqual(0.5, get_sol().frogPosition(4, [[1,2],[1,4],[2,3]], 2, 4))
    def test02(self):
        self.assertEqual(0.5, get_sol().frogPosition(4, [[1,2],[1,4],[2,3]], 3, 4))
    def test03(self):
        self.assertEqual(0.0, get_sol().frogPosition(6, [[2,1],[4,1],[5,1],[3,1],[6,3]], 7, 3))
    def test04(self):
        self.assertEqual(1.0, get_sol().frogPosition(1, [], 1, 1))
    def test05(self):
        self.assertEqual(0.0, get_sol().frogPosition(9, [[2,1],[3,2],[4,3],[5,3],[6,5],[7,3],[8,4],[9,5]], 9, 1))
    def test06(self):
        self.assertEqual(0.0, get_sol().frogPosition(5, [[2,1],[3,2],[5,3],[4,5]], 4, 1))
    def test07(self):
        self.assertEqual(0.16666666666666667, get_sol().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))
    def test08(self):
        self.assertEqual(0.0, get_sol().frogPosition(9, [[2,1],[3,1],[4,2],[5,3],[6,5],[7,4],[8,7],[9,7]], 1, 8))
    def test09(self):
        self.assertEqual(0.16666666666666667, get_sol().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4))
    def test10(self):
        self.assertEqual(0.3333333333333333, get_sol().frogPosition( 7,[[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1,  7))
