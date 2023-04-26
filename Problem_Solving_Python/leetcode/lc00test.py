from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        MOUSE,CAT,DRAW=1,-1,0
        def minimax(mPos,cPos,player):
            state=(mPos,cPos,player)
            if state in dp:
                return dp[state]
            if state in vis:
                return DRAW
            vis.add(state)
            if mPos==0:
                return MOUSE
            if cPos==mPos:
                if cPos!=0:
                    return CAT
                return DRAW
            if player==MOUSE:
                res=CAT
                for newPos in graph[mPos]:
                    tmp=minimax(newPos,cPos,CAT)
                    res=max(res,tmp)
            else:
                res=MOUSE
                for newPos in graph[cPos]:
                    tmp=minimax(mPos,newPos,MOUSE)
                    res=min(res,tmp)
            dp[state]=res
            return res

        vis=set()
        dp={}
        res=minimax(1,2,MOUSE)
        if res==-1: return 2
        return res

class Correct:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        MOUSE,CAT,DRAW=1,-1,0 # MOUSE is maximizing agent and CAT is minimizing agent
        @cache
        def search(t, x, y): # t: time, x: mousePos, y: catPos
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


class Tester(unittest.TestCase):
    def test01(self):
        a=[[2,3],[3,4],[0,4],[0,1],[1,2]]
        self.assertEqual(Correct().catMouseGame(a), Solution().catMouseGame(a))
