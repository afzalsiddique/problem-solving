import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=fkSq0QE5C_0
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        set1,set2=set(),set()
        di=defaultdict(int)
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1: set1.add((i,j))
                if img2[i][j]==1: set2.add((i,j))

        for i1,j1 in set1:
            for i2,j2 in set2:
                di[i2-i1,j2-j1]+=1

        return max(di.values()) if di else 0
class Solution2:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        set1,set2=set(),set()
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1: set1.add((i,j))
                if img2[i][j]==1: set2.add((i,j))

        ans=0
        for x in range(-n+1,n):
            for y in range(-n+1,n):
                tmp = 0
                for i,j in set1:
                    if (i+x,j+y) in set2:
                        tmp+=1
                ans=max(ans,tmp)

        return ans

class tester(unittest.TestCase):
    def test01(self):
        img1 = [[1,1,0],[0,1,0],[0,1,0]]
        img2 = [[0,0,0],[0,1,1],[0,0,1]]
        Output= 3
        self.assertEqual(Output,get_sol().largestOverlap(img1,img2))
    def test02(self):
        img1 = [[1]]
        img2 = [[1]]
        Output= 1
        self.assertEqual(Output,get_sol().largestOverlap(img1,img2))
    def test03(self):
        img1 = [[0]]
        img2 = [[0]]
        Output= 0
        self.assertEqual(Output,get_sol().largestOverlap(img1,img2))
