from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    # https://leetcode.com/problems/candy/discuss/135698/Simple-solution-with-one-pass-using-O(1)-space/409593
    def candy(self, ratings: List[int]) -> int:
        if not ratings:
            return 0
        rst = 1
        up = 1 # up=1 but down = 0. because peak is included in the up but not included in down
        down = peak = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                up += 1
                peak = up
                down = 0
                rst += up
            elif ratings[i] == ratings[i - 1]:
                up = 1
                down = 0
                peak = 0
                rst += 1
            else:
                up = 1
                down += 1
                rst += down
                if peak <= down: # if peak is not large enough, then we need to make peak larger
                    rst += 1
        return rst
class Solution5:
    # https://leetcode.com/problems/candy/discuss/42770/One-pass-constant-space-Java-solution/162756
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        start=0
        res=1
        i=0
        while i+1<n:
            while i+1<n and ratings[i+1]>ratings[i]:
                i+=1
            left=i-start

            start=i
            while i+1<n and ratings[i+1]<ratings[i]:
                i+=1
            right=i-start

            peak = max(left,right)+1
            res+=((left+1)*left)//2 + ((right+1)*right)//2 + peak -1

            while i+1<n and ratings[i+1]==ratings[i]:
                i+=1
                res+=1
            start=i
        return res
class Solution4:
    def helper(self, A:List[int]):
        res=[1]*len(A)
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                res[i]=res[i-1]+1
        return res
    def candy(self, ratings: List[int]) -> int:
        res1=self.helper(ratings)
        res2=self.helper(ratings[::-1])[::-1]
        return sum(max(x,y) for x,y in zip(res1,res2))

class Solution2:
    # https://www.youtube.com/watch?v=h6_lIwZYHQw
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        if n==1: return 1
        left,right=[1]*n,[1]*n
        for i in range(n):
            if i>0 and ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        for i in reversed(range(n)):
            if i < n-1 and ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
        maxx=[max(left[i],right[i]) for i in range(n)]
        print(ratings)
        print(maxx)
        return sum(maxx)
class Solution3:
    # wrong
    def helper(self,ratings:List[int]):
        n=len(ratings)
        res=[1]*n
        minn=min(ratings)
        idx=ratings.index(minn)
        for i in range(idx-1,-1,-1):
            if ratings[i]>ratings[i+1]:
                res[i]=res[i+1]+1
        for i in range(idx,n):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        return res
    def candy(self, ratings: List[int]) -> int:
        res1=self.helper(ratings)
        res2=self.helper(ratings[::-1])[::-1]
        print(ratings)
        print(res1)
        print(res2)
        return sum(max(x,y) for x,y in zip(res1,res2))

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(5,get_sol().candy([1,0,2]))
    def test02(self):
        self.assertEqual(4,get_sol().candy([1,2,2]))
    def test03(self):
        self.assertEqual(7,get_sol().candy([1,3,2,2,1]))
    def test04(self):
        self.assertEqual(13,get_sol().candy([1,2,87,87,87,2,1]))
    def test05(self):
        self.assertEqual(12,get_sol().candy([29,51,87,87,72,12]))
    def test06(self):
        self.assertEqual(12,get_sol().candy([1,2,3,4]))
