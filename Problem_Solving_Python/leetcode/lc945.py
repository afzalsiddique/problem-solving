import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution2()
# class Solution:
#     union find
#     def minIncrementForUnique(self, nums: List[int]) -> int:

class Solution:
    def minIncrementForUnique(self, A):
        c = Counter(A)
        res = need = 0
        for x in sorted(c):
            res += c[x] * max(need - x, 0) + c[x] * (c[x] - 1) / 2
            need = max(need, x) + c[x]
        return res
class Solution2:
    def minIncrementForUnique(self, A):
        c = Counter(A)
        res=[0]
        need=[0]
        for x in sorted(c):
            res.append(c[x] * max(need[-1] - x, 0) + c[x] * (c[x] - 1) / 2)
            need.append(max(need[-1],x)+c[x])
        print(sorted(c.keys()))
        print(need)
        print(res)
        return int(sum(res))
class Solution3:
    # time O(nlogn)
    # spcae O(1)
    def minIncrementForUnique(self, A):
        if not A: return 0
        A.sort()
        res = 0
        need=A[0]+1
        for i in range(1,len(A)):
            x=A[i]
            res+=max(need-x,0)
            need=max(need+1,x+1)
        return res
class Solution4:
    # time O(nlogn)
    # spcae O(n)
    def minIncrementForUnique(self, A):
        if not A: return 0
        A.sort()
        res = [0]
        need=[A[0]+1]
        for i in range(1,len(A)):
            x=A[i]
            res.append(max(need[-1] - x, 0))
            need.append(max(need[-1]+1,x+1))
        # print(A)
        # print(res)
        # print(need)
        return sum(res)
class Solution5:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        BIG=40000
        count = Counter(nums)
        ans=0
        for i in range(BIG*2):
            if i in count and count[i]>1:
                ans+=count[i]-1
                count[i+1]+=count[i]-1
        return ans

class MyTestCase(unittest.TestCase):
    def test_01(self):
        nums = [1,2,2]
        Output= 1
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_02(self):
        nums = [3,2,1,2,1,7]
        Output= 6
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_03(self):
        nums = [0,0]
        Output= 1
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_04(self):
        nums = [4,4,4,5,5,5,15,15,15,16,16]
        Output= 20
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_05(self):
        nums = [3,2,1,2,1,7]
        Output= 6
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    def test_06(self):
        nums = []
        Output= 0
        self.assertEqual(Output,get_sol().minIncrementForUnique(nums))
    # def test_07(self):
    # def test_08(self):
