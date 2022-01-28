import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
### SEE LEETCODE 363
class Solution:
    def getJustBeforeNextSmaller(self, A, default, cnt=1):
        n=len(A)
        nextSmaller= [default] * n
        st=[]
        for i in range(n):
            while st and A[st[-1]]> A[i]: # nextSmaller, so it is going to be increasing stack. A[st[-1]]>A[i] -> take out while the top element is greater
                nextSmaller[st.pop()]=i-cnt
            st.append(i)
        return nextSmaller
    def getJustAfterPrevSmaller(self, A): # get indices which is right before the next smaller element
        n=len(A)
        tmp= self.getJustBeforeNextSmaller(A[::-1], 0, -1)
        nextSmaller=[(0 if x==0 else n-x+1) for x in tmp]
        return nextSmaller[::-1]
    def largestRectangleArea(self, A: List[int]) -> int: # leetcode 84
        n=len(A)
        nextSmaller= self.getJustBeforeNextSmaller(A, n - 1)
        prevSmaller=self.getJustAfterPrevSmaller(A)
        res=float('-inf')
        for i in range(n):
            width=nextSmaller[i]-prevSmaller[i]+1
            res=max(res,width*A[i])
        return res
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        if not m: return 0
        n=len(matrix[0])
        res=float('-inf')
        pre=[0]*n # prefix sum
        for row in matrix:
            row=list(map(int,row))
            pre=[(pre[i]+1) if row[i]!=0 else 0 for i in range(n)]
            res=max(res,self.largestRectangleArea(pre))
        return res
class Solution2:
    # https://www.youtube.com/watch?v=dAVF2NpC3j4
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if not m:return 0
        n = len(matrix[0])
        new_mat = [[0]*n for _ in range(m)]
        for j in range(n):
            new_mat[0][j] = int(matrix[0][j])
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j]=='0':
                    new_mat[i][j]=0
                else:
                    new_mat[i][j]=new_mat[i-1][j]+int(matrix[i][j])
        mx_area = 0
        for row in new_mat:
            mx_area = max(mx_area, self.largestRectangleArea(row))
        return mx_area
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, n,mx_area= [], len(heights),0
        left,right=[0 for _ in range(n)],[0 for _ in range(n)]

        for i in range(n):
            if not stack:
                left[i]=0 # if stack is empty then there is no left bound which means the left bound is 0
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]: # it's "<=" and not "<". Run this Case: [1,5,5,5,1]
                    stack.pop()
                left[i]=stack[-1]+1 if stack else 0 # if stack is empty then there is no left bound which means the left bound is 0
                stack.append(i)
        # print(left)
        stack = []
        for i in reversed(range(n)):
            if not stack:
                right[i]=n-1 # if stack is empty then there is no right bound which means the right bound is n-1
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]:# it's "<=" and not "<". Run this Case: [1,5,5,5,1]
                    stack.pop()
                right[i]=stack[-1]-1 if stack else n-1 # if stack is empty then there is no right bound which means the right bound is n-1
                stack.append(i)
        # print(right)
        for i,h in enumerate(heights):
            mx_area = max(mx_area,(right[i]-left[i]+1)*h)
        return mx_area


class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(6,Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    def test2(self):
        self.assertEqual(0,Solution().maximalRectangle([]))
    def test3(self):
        self.assertEqual(1,Solution().maximalRectangle([['1']]))
