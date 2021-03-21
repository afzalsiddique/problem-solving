import unittest
from heapq import *
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m,n=len(image), len(image[0])
        srcColor= image[sr][sc]

        def dfs(i, j):
            if i>=m or i<0 or j>=n or j<0:
                return
            if image[i][j]==newColor:return # test 2 will fail if this line is omitted
            if image[i][j]==srcColor:
                image[i][j]=newColor
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    r,c=i+dr,j+dc
                    dfs(r,c)

        dfs(sr,sc)
        return image


class mytestcase(unittest.TestCase):
    def test_1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        newColor = 2
        e = Solution().floodFill(image, sr,sc,newColor)
        self.assertEqual([[2,2,2],[2,2,0],[2,0,1]],e)
    def test_2(self):
        image = [[1,1],[1,1]]
        sr = 0
        sc = 0
        newColor = 1
        e = Solution().floodFill(image, sr,sc,newColor)
        self.assertEqual([[1,1],[1,1]],e)
