from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

class Solution:
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
