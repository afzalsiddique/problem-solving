import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        vis = set()
        q = deque([0]) # 0 based
        res = 0
        target = n*n-1 # 0 based
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur in vis: continue
                if cur == target: return res
                vis.add(cur)
                for i in range(1,6+1):
                    tmp = cur+i
                    if tmp>n*n: continue # out of board
                    x = n-1-tmp//n
                    y= tmp%n
                    if n%2==x%2: # change direction
                        y = n-1-y
                    if board[x][y]!=-1: # use ladder or snake
                        tmp = board[x][y]
                        tmp-=1
                    q.append(tmp)
            res+=1
        return -1
class MyTestCase(unittest.TestCase):
    def test1(self):
        board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
        Output= 4
        self.assertEqual(Output, get_sol().snakesAndLadders(board))
    def test2(self):
        board = [[-1,-1],[-1,3]]
        Output= 1
        self.assertEqual(Output, get_sol().snakesAndLadders(board))