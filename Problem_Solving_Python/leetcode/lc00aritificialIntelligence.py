import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize

obstacles = [[0,1],[1,1],[2,1],[3,3],[2,3],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[1,10],[1,11],[1,12],[1,13]]
M,N=5,15
src=(0,0)
# goal=(4,0)
goal=(2,4)
EMPTY=11
BOX=99
VISITED=-1
def createGrid(M,N,obstacles): # 0 -> empty, 1-> obstacle
    grid=[[EMPTY]*N for _ in range(M)]
    for x,y in obstacles:
        grid[x][y]=BOX
    return grid

def dijkstra(grid:List[List[int]],src,goal,vis):
    def dist(x,y):
        dx=abs(src[0]-x)
        dy=abs(src[1]-y)
        return dx*dx+dy*dy
        # return math.sqrt(dx*dx+dy*dy)
    M,N=len(grid),len(grid[0])
    x,y=src
    # vis.add((x,y))
    pq=[(0,x,y)]
    while pq:
        cur,x,y=heappop(pq)
        if grid[x][y]==BOX: continue
        if (x,y) in vis: continue
        vis.add((x, y))
        if goal[0]==x and goal[1]==y: return cur
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,1)]:
        # for dx,dy in [(1,0)]:
            newX=x+dx
            newY=y+dy
            if not 0<=newX<M or not 0<=newY<N: continue
            cost = dist(newX,newY)
            # if (newX,newY) not in vis:
            #     vis.add((newX,newY))
            heappush(pq,(cost,newX,newY))


vis=set()
grid=createGrid(M,N,obstacles)
print(dijkstra(grid,src,goal,vis))
newGrid=createGrid(M,N,obstacles)
for x,y in vis:
    newGrid[x][y]=VISITED
for x in newGrid:
    print(x)
