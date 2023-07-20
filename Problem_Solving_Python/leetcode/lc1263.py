from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # PERSON POSITION AND BOX POSITION IS ENOUGH TO REPRESENT A STATE
    # after pushing the box, the person's new position is the old position of the box
    def minPushBox(self, grid: List[List[str]]) -> int:
        def withinAndNoObstacleAndNoBox(x:int,y:int,b_x:int,b_y:int)->bool:
            return 0<=x<len(grid) and 0<=y<len(grid[0]) and [x,y]!=[b_x,b_y] and grid[x][y]!='#'
        def get_4d_moves(x:int, y:int,b_x,b_y)->List[tuple[int,int]]:
            return [(x+dx,y+dy) for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)] if withinAndNoObstacleAndNoBox(x+dx,y+dy,b_x,b_y)]

        # whether person can reach (x,y) while box is lying at (b_x,b_y)
        # the box is changing position, so it must be passed as parameter
        def canReach(p_x, p_y, b_x, b_y, x, y):
            vis=set()
            q=deque([(p_x, p_y)])
            while q:
                p_x,p_y=q.popleft()
                if grid[p_x][p_y]=='#': continue
                if [p_x,p_y]==[x, y]:
                    return True
                if (p_x,p_y) in vis: continue
                vis.add((p_x,p_y))
                q.extend(get_4d_moves(p_x,p_y,b_x,b_y))
            return False
        # Whether person at (p_x,p_y) push the box at (b_x,b_y) in the direction (dx,dy)
        def canPush(p_x, p_y, b_x, b_y, dx, dy):
            # video note
            X,Y= b_x + dx, b_y + dy
            if not withinAndNoObstacleAndNoBox(X,Y,b_x,b_y): # obstacles or box found
                return False
            # in order to push the box the person must be able to reach the cell that is opposite to the direction pushing
            X,Y= b_x - dx, b_y - dy
            tmp= canReach(p_x, p_y, b_x, b_y, X, Y)
            return tmp

        m,n=len(grid),len(grid[0])
        DIRS=[[1,0],[-1,0],[0,1],[0,-1]]
        p_x,p_y=[[i,j] for i in range(m) for j in range(n) if grid[i][j]=='S'][0] # person position
        b_x,b_y=[[i,j] for i in range(m) for j in range(n) if grid[i][j]=='B'][0] # box position
        target_x,target_y=[[i,j] for i in range(m) for j in range(n) if grid[i][j]=='T'][0] # target position
        q=deque()
        q.append((p_x,p_y,b_x,b_y)) # ******* ENOUGH TO REPRESENT A STATE ************
        vis=set()
        res=0
        while q:
            for _ in range(len(q)):
                state=q.popleft()
                p_x,p_y,b_x,b_y=state
                if [b_x,b_y]==[target_x,target_y]:
                    return res
                if state in vis:
                    continue
                vis.add(state)
                for dx,dy in DIRS:
                    if not canPush(p_x, p_y, b_x, b_y, dx, dy):
                        continue
                    q.append((b_x,b_y,b_x+dx,b_y+dy)) # now the person is at the box position

            res+=1
        return -1

class Solution2:
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
        self.assertEqual(7,get_sol().minPushBox([[".",".","T","#",".","."],[".",".",".","#","B","."],["#",".",".",".",".","."],["#",".",".","#",".","S"]]))
    def test5(self):
        self.assertEqual(7,get_sol().minPushBox([["#",".",".","#","#","#","#","#"],["#",".",".","T","#",".",".","#"],["#",".",".",".","#","B",".","#"],["#",".",".",".",".",".",".","#"],["#",".",".",".","#",".","S","#"],["#",".",".","#","#","#","#","#"]]))
    def test6(self):
        self.assertEqual(-1,get_sol().minPushBox([["#","S","#",".","B","T","#"]]))
    def test7(self):
        self.assertEqual(-1,get_sol().minPushBox([["#","#","#","#","#","#","#"],["#","S","#",".","B","T","#"],["#","#","#","#","#","#","#"]]))
    # def test8(self):
