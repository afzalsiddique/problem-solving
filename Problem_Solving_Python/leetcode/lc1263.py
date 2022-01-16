import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # bfs
    def minPushBox(self, grid: List[List[str]]) -> int:
        def push(playerX, playerY, bx, by):
            dx= bx - playerX
            dy= by - playerY
            newBx,newBy= bx+dx,by+dy
            if not 0 <= newBx < m or not 0 <= newBy < n:
                return None
            if grid[newBx][newBy]=='#':
                return None
            if grid[playerX][playerY]=='#':
                return None
            if not 0<=newBx<m or not 0<=newBy<n:
                return None
            return [bx,by,newBx,newBy]
        def playerCanReachCellsAdjacentToBox(playerX, playerY, targetX, targetY, boxX, boxY, vis):
            if not 0 <= playerX < m or not 0 <= playerY < n:
                return False
            if grid[playerX][playerY]== '#':
                return False
            if [playerX, playerY]==[boxX, boxY]: # player can not go through box to reach a cell which is adjacent to box
                return False
            if grid[targetX][targetY]=='#':
                return False
            if playerX==targetX and playerY==targetY:
                return True
            if (playerX, playerY) in vis:
                return False
            vis.add((playerX, playerY))
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                newX,newY= playerX + dx, playerY + dy
                if not 0<=newX<m or not 0<=newY<n:
                    continue
                if playerCanReachCellsAdjacentToBox(newX, newY, targetX, targetY, boxX, boxY, vis):
                    return True
            return False
        def getAdjacentCellsToBox(playerX, playerY, bx, by):
            res=[]
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                newBx,newBy= bx+dx,by+dy
                if not 0<=newBx<m or not 0<=newBy<n:
                    continue
                if grid[newBx][newBy]=='#':
                    continue
                if playerCanReachCellsAdjacentToBox(playerX, playerY, newBx, newBy, bx, by, set()):
                    res.append((newBx,newBy))
            return res
        def getNext(playerX, playerY, bx, by):
            li=getAdjacentCellsToBox(playerX, playerY, bx, by)
            res=[]
            for playerX,playerY in li:
                tmp = push(playerX,playerY,bx,by)
                if tmp is None: continue
                res.append(tmp)
            return res

        m,n=len(grid),len(grid[0])
        playerX,playerY,boxX,boxY,targetX,targetY=-1,-1,-1,-1,-1,-1
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='S':
                    playerX,playerY=[i,j]
                elif grid[i][j]=='B':
                    boxX,boxY=[i,j]
                elif grid[i][j]=='T':
                    targetX,targetY=[i,j]

        vis=set()
        q=deque()
        q.append([playerX,playerY,boxX,boxY])
        res=0
        while q:
            for _ in range(len(q)):
                playerX,playerY,boxX,boxY=q.popleft()
                if (playerX,playerY,boxX,boxY) in vis: continue
                vis.add((playerX,playerY,boxX,boxY))
                if [boxX,boxY]==[targetX,targetY]:
                    return res
                nexts=getNext(playerX,playerY,boxX,boxY)
                for nxt in nexts:
                    q.append(nxt)
            res+=1
        return -1

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3,get_sol().minPushBox([["#","#","#","#","#","#"], ["#","T","#","#","#","#"], ["#",".",".","B",".","#"], ["#",".","#","#",".","#"], ["#",".",".",".","S","#"], ["#","#","#","#","#","#"]]))
    def test2(self):
        self.assertEqual(-1,get_sol().minPushBox([["#","#","#","#","#","#"], ["#","T","#","#","#","#"], ["#",".",".","B",".","#"], ["#","#","#","#",".","#"], ["#",".",".",".","S","#"], ["#","#","#","#","#","#"]]))
    def test3(self):
        self.assertEqual(5,get_sol().minPushBox( [["#","#","#","#","#","#"], ["#","T",".",".","#","#"], ["#",".","#","B",".","#"], ["#",".",".",".",".","#"], ["#",".",".",".","S","#"], ["#","#","#","#","#","#"]]))
    def test4(self):
        self.assertEqual(7,get_sol().minPushBox([["#",".",".","#","#","#","#","#"],["#",".",".","T","#",".",".","#"],["#",".",".",".","#","B",".","#"],["#",".",".",".",".",".",".","#"],["#",".",".",".","#",".","S","#"],["#",".",".","#","#","#","#","#"]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
