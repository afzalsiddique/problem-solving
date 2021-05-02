import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=set()
        def dfs(i):
            if i in vis: return
            vis.add(i)
            for neigh in rooms[i]:
                dfs(neigh)

        dfs(0)
        return True if len(vis)==len(rooms) else False

def get_sol_obj():
    return Solution()
class tester(unittest.TestCase):
    def test01(self):
        Input= [[1],[2],[3],[]]
        Output= True
        self.assertEqual(Output,get_sol_obj().canVisitAllRooms(Input))
    def test02(self):
        Input= [[1,3],[3,0,1],[2],[0]]
        Output= False
        self.assertEqual(Output,get_sol_obj().canVisitAllRooms(Input))