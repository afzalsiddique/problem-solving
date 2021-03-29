from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

class Solution:
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
