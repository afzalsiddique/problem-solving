from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/cat-and-mouse/discuss/298937/DP-memory-status-search-search-strait-forward-and-easy-to-understand
    def catMouseGame(self, graph: List[List[int]]) -> int:
        MOUSE,CAT,DRAW=1,-1,0 # MOUSE is maximizing agent and CAT is minimizing agent
        @cache
        def search(t, x, y): # t: time, x: mousePos, y: catPos
            # It takes 2 units of time for both the mouse and cat to visit 1 node each. In 2n time, both will have visited all nodes.
            # If both have visited all nodes and neither have won yet -> draw.
            if t == len(graph) * 2: # there is loop
                return 0
            if x == y:
                return CAT
            if x == 0:
                return MOUSE
            if t%2==0: # mouse's turn.
                ans=-1
                for newX in graph[x]:
                    ans=max(ans,search(t+1, newX, y))
                    if ans==MOUSE:
                        break
                return ans
            else: # cat's turn
                ans=1
                for newY in graph[y]:
                    if newY==0: continue # cat cant move to hole
                    ans=min(ans,search(t + 1, x, newY))
                    if ans==CAT:
                        break
                return ans

        ans=search(0, 1, 2)
        if ans==MOUSE:
            return 1
        elif ans==CAT:
            return 2
        return 0
class Solution2:
    # https://leetcode.com/problems/cat-and-mouse/discuss/298937/DP-memory-status-search-search-strait-forward-and-easy-to-understand
    def catMouseGame(self, graph: List[List[int]]) -> int:
        MOUSE,CAT,DRAW=1,-1,0 # MOUSE is maximizing agent and CAT is minimizing agent
        def search(t, x, y):
            if t == len(graph) * 2: return 0
            if x == y:
                dp[t,x,y] = CAT
                return CAT
            if x == 0:
                dp[t,x,y] = MOUSE
                return MOUSE
            if (t,x,y) in dp: return dp[t,x,y]
            if t%2==0:# mouse's turn
                ans=-1
                for newX in graph[x]:
                    ans=max(ans,search(t+1, newX, y))
                    if ans==MOUSE:
                        break
            else:# cat's turn
                ans=1
                for newY in graph[y]:
                    if newY==0: continue # cat cant move to hole
                    ans=min(ans,search(t + 1, x, newY))
                    if ans==CAT:
                        break
            dp[t,x,y]=ans
            return ans


        dp={}
        ans=search(0, 1, 2)
        if ans==MOUSE:
            return 1
        elif ans==CAT:
            return 2
        return 0

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, get_sol().catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))
    def test2(self):
        self.assertEqual(1, get_sol().catMouseGame([[1,3],[0],[3],[0,2]]))
    def test3(self):
        self.assertEqual(1, get_sol().catMouseGame([[6],[4,11],[9,12],[5],[1,5,11],[3,4,6],[0,5,10],[8,9,10],[7],[2,7,12],[6,7],[1,4],[2,9]]))
    def test4(self):
        self.assertEqual(1, get_sol().catMouseGame([[2,3],[3,4],[0,4],[0,1],[1,2]]))
    def test5(self):
        self.assertEqual(2, get_sol().catMouseGame([[5,6],[3,4],[6],[1,4,5],[1,3,5],[0,3,4,6],[0,2,5]]))
    # def test6(self):
    # def test7(self):
    # def test8(self):
