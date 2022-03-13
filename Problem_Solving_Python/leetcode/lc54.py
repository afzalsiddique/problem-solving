from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        EXPLORED=-999
        m,n=len(matrix),len(matrix[0])
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        dir=0
        res=[]
        x,y=0,0
        while len(res)!=m*n:
            res.append(matrix[x][y])
            matrix[x][y]=EXPLORED
            x,y=x+dirs[dir][0],y+dirs[dir][1] # move one step forward
            if x==m or y==n or matrix[x][y]==EXPLORED: # out of bounds or already explored
                x,y=x-dirs[dir][0],y-dirs[dir][1] # move back one step
                dir=(dir+1)%4 # change direction
                x,y=x+dirs[dir][0],y+dirs[dir][1] # move one step forward
        return res
class Solution2:
    # https://www.youtube.com/watch?v=1ZGJzvkcLsA
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        top,down,left,right = 0,m-1,0,n-1
        dir = 0
        res = []
        while left<=right and top<=down:
            if dir==0:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
            elif dir==1:
                for i in range(top,down+1):
                    res.append(matrix[i][right])
                right-=1
            elif dir==2:
                for i in reversed(range(left,right+1)):
                    res.append(matrix[down][i])
                down-=1
            elif dir==3:
                for i in reversed(range(top,down+1)):
                    res.append(matrix[i][left])
                left+=1
            dir = (dir+1) % 4
        return res
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,2,3,6,9,8,7,4,5], get_sol().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    def test02(self):
        self.assertEqual([1,2,3,4,8,12,11,10,9,5,6,7], get_sol().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    def test03(self):
        self.assertEqual([2,5,4,-1,0,8], get_sol().spiralOrder([[2,5],[8,4],[0,-1]]))
