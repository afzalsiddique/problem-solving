from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# def get_sol(): return solution()
class BiPartiteMatching:
    def __init__(self,graph):
        self.graph = graph
        self.ppl = len(graph)
        self.jobs = len(graph[0])

    def bpm(self, u, matchR, seen):
        for v in range(self.jobs):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True
                if matchR[v] == -1 or self.bpm(matchR[v], matchR, seen):
                    matchR[v] = u
                    return True
        return False

    def maxBPM(self):
        matchR = [-1] * self.jobs
        result = 0
        for i in range(self.ppl):
            seen = [False] * self.jobs
            if self.bpm(i, matchR, seen):
                result += 1
        return result


def solution(A, B, S):
    m=len(A)
    if S<m: return False
    n=max(max(A),max(B))
    graph=[[0]*n for _ in range(m)]
    for i in range(m):
        # print('col:',A[i]-1)
        graph[i][A[i]-1]=1
        graph[i][B[i]-1]=1

    g = BiPartiteMatching(graph)
    ans=g.maxBPM()
    # print(ans)
    return ans>=m

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(True,solution([1,1,3],[2,2,1],3))
    def test02(self):
        self.assertEqual(False,solution([3,2,3,1],[1,3,1,2],3))
    def test03(self):
        self.assertEqual(True,solution([2,5,6,5],[5,4,2,2],8))
    def test04(self):
        self.assertEqual(False,solution([1,2,1,6,8,7,8],[2,3,4,7,7,8,7],10))
