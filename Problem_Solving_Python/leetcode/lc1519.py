import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(u): # returns array counter
            vis.add(u)
            count=[0]*26
            for v in g[u]:
                if v in vis: continue
                tmp = dfs(v)
                count = [count[i]+tmp[i] for i in range(26)]
            ch=ord(labels[u])-ord('a')
            count[ch]+=1
            res[u]=count[ch]
            return count

        vis=set()
        g=defaultdict(list)
        res=[0]*n
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)

        dfs(0)
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        n,edges,labels = 7,[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd"
        Output= [2,1,1,1,1,1,1]
        self.assertEqual(Output, get_sol().countSubTrees(n,edges,labels))
    def test_2(self):
        n,edges,labels = 4,[[0,1],[1,2],[0,3]], "bbbb"
        Output= [4,2,1,1]
        self.assertEqual(Output, get_sol().countSubTrees(n,edges,labels))
    def test_3(self):
        n,edges,labels = 5,[[0,1],[0,2],[1,3],[0,4]], "aabab"
        Output= [3,2,1,1,1]
        self.assertEqual(Output, get_sol().countSubTrees(n,edges,labels))
    def test_4(self):
        n,edges,labels = 6,[[0,1],[0,2],[1,3],[3,4],[4,5]], "cbabaa"
        Output= [1,2,1,1,2,1]
        self.assertEqual(Output, get_sol().countSubTrees(n,edges,labels))
    def test_5(self):
        n,edges,labels = 7,[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], "aaabaaa"
        Output= [6,5,4,1,3,2,1]
        self.assertEqual(Output, get_sol().countSubTrees(n,edges,labels))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):