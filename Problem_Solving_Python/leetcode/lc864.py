import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # include keyMask as part of state to overcome infinite loop and visit a cell multiple times with different keyMask
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def isSelected(mask:int,char:str):
            i = ord(char)-ord('A')
            return mask & (1<<i)
        def turnOn(mask:int, char:str):
            i=ord(char)-ord('a')
            return mask | (1<<i)
        def ifWall(char:str):
            return char=='#'
        def ifKey(char:str):
            return 'a'<=char<='f'
        def ifLock(char:str):
            return 'A'<=char<='F'

        m,n=len(grid),len(grid[0])
        startI,startJ = [(i,j) for i in range(m) for j in range(n) if grid[i][j]=='@'][0]
        noOfKeys= len([(i,j) for i in range(m) for j in range(n) if ifKey(grid[i][j])])
        goal = 2**noOfKeys-1
        vis = set()
        vis.add((startI,startJ,0))
        q= deque()
        q.append((startI,startJ,0))
        res=0
        while q:
            for _ in range(len(q)):
                i,j,keyMask=q.popleft()
                if keyMask==goal: return res
                for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                    newI,newJ = i+di,j+dj
                    if not 0<=newI<m or not 0<=newJ<n: continue
                    cell=grid[newI][newJ]
                    newKeyMask=keyMask
                    if ifKey(cell):
                        newKeyMask=turnOn(newKeyMask,cell)
                    if (newI,newJ,newKeyMask) in vis: continue
                    if ifWall(cell): continue
                    if ifLock(cell) and not isSelected(newKeyMask,cell): continue
                    q.append((newI,newJ,newKeyMask))
                    vis.add((newI,newJ,newKeyMask))
            res+=1
        return -1




class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(8, get_sol().shortestPathAllKeys(grid = ["@.a.#","###.#","b.A.B"]))
    def test2(self):
        self.assertEqual(6, get_sol().shortestPathAllKeys(grid = ["@..aA","..B#.","....b"]))
    def test3(self):
        self.assertEqual(-1, get_sol().shortestPathAllKeys(["@Aa"]))
    def test4(self):
        self.assertEqual(-1, get_sol().shortestPathAllKeys(["@abcdeABCDEFf"]))
    # def test5(self):
    # def test6(self):
    # def test7(self):

