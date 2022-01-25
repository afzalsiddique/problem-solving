from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    # longest increasing subsequence
    def longestObstacleCourseAtEachPosition(self, A: List[int]) -> List[int]:
        n=len(A)
        dp=[1]*n
        li=[]
        for i in range(n):
            idx=bisect_right(li,A[i])
            if idx==len(li):
                li.append(A[i])
            else:
                li[idx]=min(li[idx],A[i])
            dp[i]=idx+1
        return dp
class Solution2:
    # wrong. Monotonic stack can only maintain strictly increasing or strictly decreasing subsequence
    def longestObstacleCourseAtEachPosition(self, A: List[int]) -> List[int]:
        n=len(A)
        st=[]
        res=[-1]*n
        for i in range(n):
            while st and A[st[-1]]>A[i]:
                st.pop()
            res[i]=len(st)+1
            st.append(i)
        return res
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,2,3,3], get_sol().longestObstacleCourseAtEachPosition( [1,2,3,2]))
    def test02(self):
        self.assertEqual([1,2,1], get_sol().longestObstacleCourseAtEachPosition([2,2,1]))
    def test03(self):
        self.assertEqual([1,1,2,3,2,2], get_sol().longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))
    def test04(self):
        self.assertEqual([1,1,2,3,2,3,4,5,3,5], get_sol().longestObstacleCourseAtEachPosition([5,1,5,5,1,3,4,5,1,4]))
    def test05(self):
        self.assertEqual([1, 2, 1, 3], get_sol().longestObstacleCourseAtEachPosition([3,4,1,4]))
