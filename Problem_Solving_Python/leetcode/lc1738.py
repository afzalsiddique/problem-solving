from itertools import accumulate; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # prefix sum
    # https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/discuss/1032010/Detailed-Explanation-or-C%2B%2B-Solution-or-Easy-Implementation
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            matrix[i]=list(accumulate(matrix[i],lambda a,b: a^b))
        for j in range(n):
            for i in range(1,m):
                matrix[i][j]^=matrix[i-1][j]

        li=[]
        for i in range(m):
            for j in range(n):
                li.append(matrix[i][j])
        li.sort()
        return li[-k]
class Solution2:
    # https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/discuss/1032143/Java-Detailed-Explanation-DP-with-Graph-Demo
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m,n=len(matrix),len(matrix[0])
        li=[]
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=dp[i-1][j]^dp[i][j-1]^dp[i-1][j-1]^matrix[i-1][j-1]
                li.append(dp[i][j])
        li.sort()
        return li[-k]

class MyTestCase(unittest.TestCase):
    def test_1(self):
        matrix,k = [[5,2],[1,6]],1
        Output= 7
        self.assertEqual(Output, get_sol().kthLargestValue(matrix,k))
    def test_2(self):
        matrix,k = [[5,2],[1,6]],2
        Output= 5
        self.assertEqual(Output, get_sol().kthLargestValue(matrix,k))
    def test_3(self):
        matrix,k = [[5,2],[1,6]],3
        Output= 4
        self.assertEqual(Output, get_sol().kthLargestValue(matrix,k))
    def test_4(self):
        matrix,k = [[5,2],[1,6]],4
        Output= 0
        self.assertEqual(Output, get_sol().kthLargestValue(matrix,k))
    def test_5(self):
        matrix,k = [[10,9,5],[2,0,4],[1,0,9],[3,4,8]], 10
        Output= 1
        self.assertEqual(Output, get_sol().kthLargestValue(matrix,k))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
