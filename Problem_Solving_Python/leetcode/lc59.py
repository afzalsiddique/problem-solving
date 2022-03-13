from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        EMPTY=-999
        matrix=[[EMPTY]*n for _ in range(n)]
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        dir=0
        x,y=0,0
        cnt=1
        while cnt!=n*n+1:
            matrix[x][y]=cnt
            x,y=x+dirs[dir][0],y+dirs[dir][1] # move one step forward
            if x==n or y==n or matrix[x][y]!=EMPTY: # out of bounds or not empty
                x,y=x-dirs[dir][0],y-dirs[dir][1] # move back one step
                dir=(dir+1)%4 # change direction
                x,y=x+dirs[dir][0],y+dirs[dir][1] # move one step forward
            cnt+=1
        return matrix
class Solution2:
    # https://www.youtube.com/watch?v=1ZGJzvkcLsA
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        top,down,left,right = 0,n-1,0,n-1
        dir,cnt = 0,1
        while top<=down and left<=right:
            if dir==0:
                for i in range(left,right+1):
                    matrix[top][i]=cnt
                    cnt+=1
                top+=1
            elif dir==1:
                for i in range(top,down+1):
                    matrix[i][right]=cnt
                    cnt+=1
                right-=1
            elif dir==2:
                for i in reversed(range(left,right+1)):
                    matrix[down][i]=cnt
                    cnt+=1
                down-=1
            elif dir==3:
                for i in reversed(range(top,down+1)):
                    matrix[i][left]=cnt
                    cnt+=1
                left+=1
            dir = (dir+1)%4
        return matrix
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([[1,2,3],[8,9,4],[7,6,5]], get_sol().generateMatrix(3))
    def test02(self):
        self.assertEqual([[1]], get_sol().generateMatrix(1))
    # def test03(self):
