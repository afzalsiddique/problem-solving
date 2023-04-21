from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize
def get_sol(): return Solution()
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def turn_on(mask,i): return mask | (1<<i)
        def is_on(mask,i): return (mask>>i)&1 # returns 1 when True or 0 when False
        def allSelected(mask, n): return mask == ((1 << n) - 1)
        def within(x,y): return 0<=x<m and 0<=y<n
        def get_4d_moves(x,y): return [(x+dx,y+dy) for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)] if within(x+dx,y+dy)]
        def ch_to_int(ch): return ord(ch.lower())-ord('a') # ['a'->0, 'A'->0]
        def isKey(i,j): return 'a'<=grid[i][j]<='z'
        def isLock(i,j): return 'A'<=grid[i][j]<='Z'
        def isWall(i,j): return grid[i][j]=='#'
        def hasKey(mask,lock_ch): return is_on(mask,ch_to_int(lock_ch))
        def get_start_pos(): return [[x,y] for x in range(m) for y in range(n) if grid[x][y]=='@'][0]
        def no_of_keys(): return sum(isKey(x,y) for x in range(m) for y in range(n))
        def all_keys_found(mask): return allSelected(mask,NO_OF_KEYS)
        def can_go(i,j,mask): # if I can go to the next cell
            if not isLock(i,j): return True # no lock. so I can go.
            return hasKey(mask,grid[i][j]) # locked. so depends on whether I have key to this lock

        m,n=len(grid),len(grid[0])
        NO_OF_KEYS=no_of_keys()
        initialState = tuple(get_start_pos()+[0]) # (x,y,keyMask)
        q = deque()
        q.append(initialState)
        vis=set()
        res=0
        while q:
            for _ in range(len(q)):
                i,j,mask = q.popleft()
                if isWall(i,j): continue
                if not can_go(i,j,mask): continue
                if (i,j,mask) in vis: continue
                vis.add((i,j,mask))
                newMask=mask
                if isKey(i,j):
                    newMask=turn_on(mask,ch_to_int(grid[i][j]))
                if all_keys_found(newMask): return res
                for X,Y in get_4d_moves(i,j):
                    q.append((X,Y,newMask))
            res+=1
        return -1
class Solution2:
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

