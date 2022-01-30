import unittest
from heapq import *
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m,n=len(image), len(image[0])
        srcColor= image[sr][sc]

        def dfs(x, y):
            if x>=m or y>=n or x<0 or y<0: return
            if image[x][y]==newColor:return # if coloring is not required at all
            if image[x][y]!=srcColor:return
            image[x][y]=newColor
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                i,j = x + dx, y + dy
                dfs(i,j)

        dfs(sr,sc)
        return image

class Tester(unittest.TestCase):
    def test01(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        newColor = 2
        self.assertEqual([[2,2,2],[2,2,0],[2,0,1]],get_sol().floodFill(image, sr,sc,newColor))
    def test02(self):
        image = [[1,1],[1,1]]
        sr = 0
        sc = 0
        newColor = 1
        self.assertEqual([[1,1],[1,1]],get_sol().floodFill(image, sr,sc,newColor))
