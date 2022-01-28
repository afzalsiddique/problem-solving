from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://leetcode.com/problems/rotting-oranges/discuss/563686/Python-Clean-and-Well-Explained-(faster-than-greater-90)
# https://www.youtube.com/watch?v=CxrnOTUlNJE

class Solution:
    # bfs and without destroying the input
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY,FRESH,ROTTEN,VISITED=0,1,2,3
        m,n=len(grid),len(grid[0])
        rottenOranges=[[i,j] for i in range(m) for j in range(n) if grid[i][j]==ROTTEN]
        freshOranges=[[i,j] for i in range(m) for j in range(n) if grid[i][j]==FRESH]
        if not rottenOranges:
            if freshOranges:
                return -1
            return 0
        q=deque(rottenOranges)
        res=-1
        while q:
            for _ in range(len(q)):
                x,y=q.popleft()
                grid[x][y]=VISITED
                for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                    newX,newY=x+dx,y+dy
                    if not 0<=newX<m or not 0<=newY<n: continue
                    if grid[newX][newY]==VISITED: continue
                    if grid[newX][newY]==EMPTY: continue
                    if grid[newX][newY]==ROTTEN: continue
                    grid[newX][newY]=ROTTEN
                    q.append([newX,newY])
            res+=1
        freshOrangesLeft=any(grid[i][j]==FRESH for i in range(m) for j in range(n))
        for i,j in freshOranges: grid[i][j]=FRESH
        for i,j in rottenOranges: grid[i][j]=ROTTEN
        if freshOrangesLeft:
            return -1
        return res
class Solution1:
    def get_grid_state(self, grid):
        fresh, rotten = set(), set()
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                pos = (row,col)
                if grid[row][col] == 2:
                    rotten.add(pos)
                elif grid[row][col] == 1:
                    fresh.add(pos)

        return fresh, rotten

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get (row,col) for fresh and rotten oranges (as a set)
        fresh, rotten = self.get_grid_state(grid)

        # convert rotten set to list for adding it to queue
        q = deque(list(rotten))
        mins_to_rotten = 0

        # peform BFS while we have rotten oranges and fresh oranges
        while q and fresh:
            mins_to_rotten += 1

            # iterate rotten oranges at this level only
            for _ in range(len(q)):
                rotten_row, rotten_col = q.popleft()

                # iterate thru neighboring grids
                for delta_row, delta_col in [(1,0), (-1,0), (0,1), (0,-1)]:
                    next_pos = (rotten_row+delta_row, rotten_col+delta_col)
                    if next_pos in fresh:
                        # next_pos has a fresh orange. NOTE: we don't have to worry about out of bounds check since fresh will only contain valid cell positions
                        q.append(next_pos)
                        # add fresh orange to the q and remove it from the fresh set
                        # ensures a loop free BFS traversal without explicity taking care of visited positions
                        fresh.remove(next_pos)

        return -1 if len(fresh) != 0 else mins_to_rotten

class Solution4:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        FRESH,ROTTEN,INVISIBLE = 1,2,0 # Fresh apple gets rotten, rotten apple turns invisible
        fresh_apples = any([grid[i][j]==FRESH for i in range(m) for j in range(n)])
        if not fresh_apples:return 0
        q=deque([(x,y) for x in range(m) for y in range(n) if grid[x][y]==2]) # queue only contains rotten apples
        day = -1
        while q:
            day+=1
            for _ in range(len(q)):
                r,c=q.popleft() # queue only pops out rotten apple
                grid[r][c]=INVISIBLE # rotten apple turns invisible
                for (dr,dc) in [(1,0),(-1,0),(0,1),(0,-1)]:
                    i = r+dr
                    j = c + dc
                    if i < m and j < n and i>=0 and j>=0 and grid[i][j]==FRESH:
                        grid[i][j]=ROTTEN # fresh apple gets rotten
                        q.append((i,j))
        fresh_apples = any([grid[i][j]==FRESH for i in range(m) for j in range(n)]) # fresh apple remains
        return day if not fresh_apples else -1

class Solution3:
    # uses too much memory and not readable.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        fresh = any(grid[x][y]==1 for x in range(m) for y in range(n))
        if not fresh:return 0
        q=deque([(x,y) for x in range(m) for y in range(n) if grid[x][y]==2])
        rotten = set(q)
        cnt=-1
        while q:
            cnt+=1
            sett = set()
            for _ in range(len(q)):
                x,y=q.popleft()
                grid[x][y]=2
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    i,j=x+dx,y+dy
                    if i>=m or j>=n or i<0 or j<0:continue
                    if grid[i][j]==2 or grid[i][j]==0:continue
                    if (i,j) in rotten:continue
                    sett.add((i,j))
            rotten.update(sett)
            q = deque(sett)
        fresh = any(grid[i][j]==1 for i in range(m) for j in range(n))
        return cnt if not fresh else -1


class MyTestCase(unittest.TestCase):
    def test01(self):
        grid=[[2,1,1],[1,1,0],[0,1,1]]
        gridCopy=[[x for x in row] for row in grid]
        self.assertEqual(4,get_sol().orangesRotting(grid))
        self.assertEqual(gridCopy,grid) # check if the input is unchanged after operation
    def test02(self):
        grid=[[2,1,1],[0,1,1],[1,0,1]]
        gridCopy=[[x for x in row] for row in grid]
        self.assertEqual(-1,get_sol().orangesRotting(grid))
        self.assertEqual(gridCopy,grid) # check if the input is unchanged after operation
    def test03(self):
        grid=[[0,2]]
        gridCopy=[[x for x in row] for row in grid]
        self.assertEqual(0,get_sol().orangesRotting(grid))
        self.assertEqual(gridCopy,grid) # check if the input is unchanged after operation
    def test04(self):
        grid=[[2,2],[1,1],[0,0],[2,0]]
        gridCopy=[[x for x in row] for row in grid]
        self.assertEqual(1,get_sol().orangesRotting(grid))
        self.assertEqual(gridCopy,grid) # check if the input is unchanged after operation
    def test05(self):
        grid=[[0]]
        gridCopy=[[x for x in row] for row in grid]
        self.assertEqual(0,get_sol().orangesRotting(grid))
        self.assertEqual(gridCopy,grid) # check if the input is unchanged after operation
    def test06(self):
        grid=[[1]]
        gridCopy=[[x for x in row] for row in grid]
        self.assertEqual(-1,get_sol().orangesRotting(grid))
        self.assertEqual(gridCopy,grid) # check if the input is unchanged after operation
