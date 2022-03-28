from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans
class Solution2:
    def maxDistToClosest(self, seats):
        n=len(seats)
        start=0
        end=0
        i=0
        middle=0
        for i in range(n): # [0,0,0,1]
            if seats[i]==1:
                break
            start+=1
        cnt=0
        for i in range(i+1,n):
            if seats[i]==1:
                cnt+=1
                middle = max(middle,cnt)
                cnt=0
            else:
                cnt+=1
        end=cnt # [1,0,0,0]
        return max(start,end,middle//2)

class Solution3:
    def maxDistToClosest(self, A: List[int]) -> int:
        n=len(A)
        left=0
        while left<n and A[left]==0:
            left+=1
        leftMax=left
        right=n-1
        while right>=0 and A[right]==0:
            right-=1
        rightMax=n-1-right

        middleMax=float('-inf')
        i=left
        cnt=0
        while i<n:
            if A[i]==1:
                middleMax=max(middleMax,ceil(cnt/2))
                cnt=0
            else:
                cnt+=1
            i+=1
        return max(leftMax,rightMax,middleMax)
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().maxDistToClosest([1,0,0,0,1,0,1]))
    def test02_1(self):
        self.assertEqual(3, get_sol().maxDistToClosest([1,0,0,0]))
    def test02_2(self):
        self.assertEqual(3, get_sol().maxDistToClosest([0,0,0,1]))
    def test03_1(self):
        self.assertEqual(2, get_sol().maxDistToClosest([1,0,0]))
    def test03_2(self):
        self.assertEqual(2, get_sol().maxDistToClosest([0,0,1]))
    def test04(self):
        self.assertEqual(1, get_sol().maxDistToClosest([0,1]))
    def test05(self):
        self.assertEqual(1, get_sol().maxDistToClosest([1,0,0,1]))
