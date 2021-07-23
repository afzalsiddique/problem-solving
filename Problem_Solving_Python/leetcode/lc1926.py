import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def out_of_maze(i,j):
            if not 0<=i<m or not 0<=j<n: return True
            return False
        def in_boundary(i,j):
            if i==0 or i==m-1 or j==0 or j==n-1: return True
            return False
        m,n=len(maze),len(maze[0])

        vis=set()
        q=deque()
        q.append((entrance[0],entrance[1]))
        depth=0
        while q:
            for _ in range(len(q)):
                i,j=q.popleft()
                if (i,j) in vis:continue
                vis.add((i,j))
                if depth!=0 and in_boundary(i,j):
                    return depth
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if not out_of_maze(i+di,j+dj) and maze[i+di][j+dj]=='.':
                        q.append((i+di,j+dj))
            depth+=1
        return -1



class tester(unittest.TestCase):
    def test_1(self):
        maze = [["+","+",".","+"],
                [".",".",".","+"],
                ["+","+","+","."]]
        entrance = [1,2]
        Output= 1
        self.assertEqual(Output,get_sol().nearestExit(maze,entrance))
    def test_2(self):
        maze = [["+","+","+"],[".",".","."],["+","+","+"]]
        entrance = [1,0]
        Output= 2
        self.assertEqual(Output,get_sol().nearestExit(maze,entrance))
    def test_3(self):
        maze = [[".","+"]]
        entrance = [0,0]
        Output= -1
        self.assertEqual(Output,get_sol().nearestExit(maze,entrance))
    def test_4(self):
        maze = [["."]]
        entrance = [0,0]
        Output= -1
        self.assertEqual(Output,get_sol().nearestExit(maze,entrance))
    def test_5(self):
        maze = [[".",".",".",".",".","+",".",".","."],[".","+",".",".",".",".",".",".","."],[".",".","+",".","+",".","+",".","+"],[".",".",".",".","+",".",".",".","."],[".",".",".",".","+","+",".",".","."],["+",".",".",".",".",".",".",".","."],[".",".",".","+",".",".",".",".","."],[".",".",".","+",".",".",".",".","+"],["+",".",".","+",".","+","+",".","."]]
        entrance = [8,4]
        Output= 'not sure'
        self.assertEqual(Output,get_sol().nearestExit(maze,entrance))
    def test_6(self):
        maze = [["+",".","+","+","+","+","+"],
                ["+",".","+",".",".",".","+"],
                ["+",".","+",".","+",".","+"],
                ["+",".",".",".",".",".","+"],
                ["+","+","+","+",".","+","."]]
        entrance = [0,1]
        Output= 7
        self.assertEqual(Output,get_sol().nearestExit(maze,entrance))
    def test_7(self):
        maze = [["+",".",".","+",".",".",".",".",".","+",".","+","+","+","+","+",".",".",".","."],[".","+",".",".",".","+",".","+",".",".","+","+",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","+",".",".",".",".",".","+",".",".",".","+"],["+",".",".","+",".","+","+","+",".","+",".",".",".",".","+","+",".",".",".","."],[".","+",".",".",".","+",".",".",".","+",".",".","+",".",".",".",".",".",".","."],["+",".","+","+",".",".",".",".",".",".",".",".",".",".","+",".",".","+","+","."],[".",".",".",".","+",".","+","+",".",".",".",".","+","+","+",".",".",".",".","."],[".","+",".",".",".","+",".",".","+",".","+",".",".","+","+",".","+",".",".","+"],[".",".",".",".",".",".",".",".",".",".",".","+","+","+",".",".","+",".",".","."],[".","+","+",".","+",".","+",".","+","+","+",".",".","+","+",".",".","+","+","."],[".",".",".",".",".",".","+","+","+",".",".",".","+",".","+","+","+",".","+","."],[".","+",".","+",".","+",".",".","+",".",".","+","+",".","+",".",".","+",".","."],[".","+",".",".",".","+","+",".",".","+","+","+",".",".",".","+","+","+",".","."],[".",".",".",".",".",".",".","+",".",".","+",".",".","+",".",".","+",".",".","."],[".",".","+","+",".","+",".",".","+",".",".",".",".",".","+",".",".","+",".","."],[".",".","+",".",".","+",".","+","+",".",".",".",".",".",".","+",".",".",".","."],[".",".",".",".",".",".",".",".",".",".","+",".",".",".","+",".",".","+",".","+"],[".",".",".",".","+",".",".",".",".",".","+",".",".",".",".","+",".",".",".","."]]
        entrance = [17,9]
        Output= 1
        self.assertEqual(Output,get_sol().nearestExit(maze,entrance))
