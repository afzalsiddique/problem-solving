from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution5:
    # my approach
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def get_size_dfs(u, par):
            ans=1
            for v in g[u]:
                if v==par: continue
                ans+= get_size_dfs(v,u)
            size[u]=ans
            return ans
        def get_distance_of_root(u, depth, par): # assume root to be 0
            ans=0
            for v in g[u]:
                if v==par: continue
                ans+= get_distance_of_root(v, depth + 1, u)
            return ans+depth
        def reroot_dfs(u,par):
            if par!=-1:
                #                       subtree on the other side    subtree on this side
                distance[u]=distance[par]   + (size[0]-size[u]) -       size[u]
            for v in g[u]:
                if v==par: continue
                reroot_dfs(v,u)

        size=[0]*n
        distance = [0]*n
        g=[[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        get_size_dfs(0,-1) # assume root to be 0
        distance[0]= get_distance_of_root(0, 0, -1) # assume root to be 0
        reroot_dfs(0,-1) # assume root to be 0
        # print(distance)
        return distance
class Solution:
    # https://www.youtube.com/watch?v=nGhE4Ekmzbc
    # https://www.youtube.com/watch?v=gmEsErNo84g
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def postOrder(root:int, pre:int): # calculate res and subTreeSize
            for i in tree[root]:
                if i==pre: continue
                postOrder(i,root)
                subTreeSize[root]+=subTreeSize[i]
                res[root]+=res[i]+subTreeSize[i]
            subTreeSize[root]+=1
        def preOrder(root:int, pre:int):
            for i in tree[root]:
                if i==pre: continue
                res[i]=res[root] - subTreeSize[i] + (n - subTreeSize[i])
                # res[i]=res[root] - subTreeSize[i] + (len(subTreeSize) - subTreeSize[i])
                preOrder(i,root)

        tree=defaultdict(list)
        for u,v in edges:
            tree[u].append(v)
            tree[v].append(u)

        subTreeSize=[0]*n
        res=[0]*n
        postOrder(0,-1)
        preOrder(0,-1)
        return res
class Solution2:
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
class Solution3:
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
    def test4(self):
        self.assertEqual([3,3,2], get_sol().sumOfDistancesInTree(3, [[2,1],[0,2]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
