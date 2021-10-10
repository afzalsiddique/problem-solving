import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # bad solution. time O(m*n*(m+n))
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def rotate(layer):
            top_row = layer
            bottom_row = m-1-layer
            left_col = layer
            right_col = n-1-layer
            i,j=top_row,left_col
            tmp = grid[top_row][left_col+1]
            dir = (1,0)
            while True:
                top_left = i==top_row and j==left_col
                top_right = i==top_row and j==right_col
                bottom_left = i==bottom_row and j==left_col
                bottom_right = i==bottom_row and j==right_col
                if top_left: dir = (1,0)
                elif bottom_left: dir = (0,1)
                elif bottom_right: dir = (-1,0)
                elif top_right: dir = (0,-1)
                tmp,grid[i][j]=grid[i][j],tmp
                i,j=i+dir[0],j+dir[1]
                if (i,j)==(top_row,left_col):
                    break

        m,n=len(grid),len(grid[0])
        for layer in range(min(m,n)//2):
            no_of_cells_in_layer =(m-layer*2+n-layer*2)*2-4
            no_of_rotation = k % no_of_cells_in_layer
            for _ in range(no_of_rotation):
                rotate(layer)
        return grid


class MyTestCase(unittest.TestCase):
    def test1(self):
        grid,k = [[40,10],[30,20]],  1
        Output= [[10,20],[40,30]]
        self.assertEqual(Output, get_sol().rotateGrid(grid,k))
    def test2(self):
        grid,k = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],  2
        Output= [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
        self.assertEqual(Output, get_sol().rotateGrid(grid,k))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):