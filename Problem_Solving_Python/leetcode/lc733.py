import unittest
from heapq import *
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m,n=len(image), len(image[0])

        def dfs(i, j, srcColor):
            if i>=m or i<0 or j>=n or j<0:
                return
            if image[i][j]==srcColor:
                image[i][j]=newColor
                dfs(i + 1, j, srcColor)
                dfs(i - 1, j, srcColor)
                dfs(i, j + 1, srcColor)
                dfs(i, j - 1, srcColor)

        if image[sr][sc]==newColor:return image
        dfs(sr,sc,image[sr][sc])
        return image


class case(unittest.TestCase):
    def test_1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        newColor = 2
        e = Solution().floodFill(image, sr,sc,newColor)
        self.assertEqual([[2,2,2],[2,2,0],[2,0,1]],e)
