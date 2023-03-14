from collections import defaultdict;
import unittest; from typing import List;


def get_sol(): return Solution()
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self): return str(self.val)
class Solution:
    # https://www.youtube.com/watch?v=lWCZOjUOjRc&t=717s
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs1(u:int,par:int): # calculate subDist and subSize
            subSize[u]=1
            for v in g[u]:
                if v==par: continue
                dfs1(v,u)
                subSize[u]+=subSize[v]
                subDist[u]+=subSize[v]+subDist[v]
        def dfs2(u:int,par:int):
            res[u] = res[par] - (subSize[u]+subDist[u]) + n - subSize[u] + subDist[u]
            for v in g[u]:
                if v==par: continue
                dfs2(v,u)

        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        subSize=[0]*n
        subDist=[0]*n
        res=[-1]*n
        dfs1(0,-1)
        res[0]=subDist[0]
        for v in g[0]:
            dfs2(v,0)
        return res
class Solution2:
    # tle
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        INVALID=-1
        def get_weight(u:int): # dfs
            if u in set1:
                return 0
            if len(g[u])==1 and g[u][0] in set1:
                weights[u]=1
                return 1
            set1.add(u)
            ans=1
            for v in g[u]:
                ans+=get_weight(v)
            weights[u]=ans
            return ans
        def dfs(u:int):
            if u in set2:
                return INVALID # invalid
            if len(g[u])==1 and g[u][0] in set2:
                return 0
            set2.add(u)
            ans=0
            for v in g[u]:
                tmp1=dfs(v)
                if tmp1==INVALID: continue
                tmp2=weights[v]
                ans+=tmp1+tmp2
            return ans

        g=defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        res=[]
        for i in range(n):
            set1=set()
            set2=set()
            weights=[0]*n
            get_weight(i)
            res.append(dfs(i))
        # get_weight(1) # consider 0 as root
        # return [dfs(1)]# for i in range(n)]
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([8,12,6,10,10,10], get_sol().sumOfDistancesInTree(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    def test2(self):
        self.assertEqual([0], get_sol().sumOfDistancesInTree(n = 1, edges = []))
    def test3(self):
        self.assertEqual([1,1], get_sol().sumOfDistancesInTree(n = 2, edges = [[1,0]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
