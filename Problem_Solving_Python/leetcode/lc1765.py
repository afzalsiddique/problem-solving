import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n=len(isWater),len(isWater[0])
        q = deque([(i,j) for i in range(m) for j in range(n) if isWater[i][j]])
        vis=set()
        mat=[[-1]*n for _ in range(m)]

        height=0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                if (i,j) in vis or not 0<=i<m or not 0<=j<n: continue
                vis.add((i,j))
                mat[i][j]=height
                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    q.append((i+di,j+dj))
            height+=1
        return mat


class MyTestCase(unittest.TestCase):
    def test_1(self):
        isWater = [[0,1],[0,0]]
        Output= [[1,0],[2,1]]
        self.assertEqual(Output, get_sol().highestPeak(isWater))
    def test_2(self):
        isWater = [[0,0,1],[1,0,0],[0,0,0]]
        Output= [[1,1,0],[0,1,1],[1,2,2]]
        self.assertEqual(Output, get_sol().highestPeak(isWater))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
