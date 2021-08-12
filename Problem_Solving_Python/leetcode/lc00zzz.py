import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        def h(i,j):
            if not 0<=i<m or not 0<=j<n: return 0,0
            if (i,j) in dp_pos: return dp_pos[i,j], dp_neg[i,j]
            if (i,j)==(m-1,n-1):
                if grid[i][j]>0:
                    dp_pos[i,j]=grid[i][j]
                    dp_neg[i,j]=0
                elif grid[i][j]<0:
                    dp_neg[i,j]=grid[i][j]
                    dp_pos[i,j]=0
                else:
                    dp_pos[i,j]=0
                    dp_neg[i,j]=0
                return dp_pos[i,j],dp_neg[i,j]
            for di,dj in [(1,0),(0,1)]:
                ans_pos,ans_neg=h(i+di,j+dj)
                if grid[i][j]>0:
                    if ans_pos!=0:
                        dp_pos[i,j]=max(dp_pos[i,j],ans_pos*grid[i][j])
                    else:
                        dp_pos[i,j]=max(dp_pos[i,j],grid[i][j])
                    if ans_neg!=0:
                        dp_neg[i,j]=min(dp_neg[i,j],ans_neg*grid[i][j])
                    else:
                        dp_neg[i,j]=min(dp_neg[i,j],grid[i][j])
                elif grid[i][j]<0:
                    if ans_neg!=0:
                        dp_pos[i,j]=max(dp_pos[i,j],ans_neg*grid[i][j])
                    else:
                        dp_pos[i,j]=max(dp_pos[i,j],0)
                    if ans_pos!=0:
                        dp_neg[i,j]=min(dp_neg[i,j],ans_pos*grid[i][j])
                    else:
                        dp_neg[i,j]=min(dp_neg[i,j],0)
                else:
                    dp_pos[i,j]=max(dp_pos[i,j],0)
                    dp_neg[i,j]=min(dp_neg[i,j],0)
            return dp_pos[i,j],dp_neg[i,j]

        m,n=len(grid),len(grid[0])
        dp_pos=defaultdict(lambda:float('-inf'))
        dp_neg=defaultdict(lambda:float('inf'))
        h(0,0)
        print(dp_pos)
        print(dp_neg)
        ans=dp_pos[0,0]
        return ans if ans>0 else -1

class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid = [[-1,-2,-3], [-2,-3,-3], [-3,-3,-2]]
        Output= -1
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_2(self):
        grid = [[1,-2,1], [1,-2,1], [3,-4,1]]
        Output= 8
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_3(self):
        grid = [[1, 3], [0,-4]]
        Output= 0
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    def test_4(self):
        grid = [[ 1, 4,4,0], [-2, 0,0,1], [ 1,-1,1,1]]
        Output= 2
        self.assertEqual(Output, get_sol().maxProductPath(grid))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
